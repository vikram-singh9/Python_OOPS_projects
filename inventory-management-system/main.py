import streamlit as st
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize SQLAlchemy
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    category = Column(String(50))
    last_updated = Column(DateTime, default=datetime.now)

class InventoryManager:
    def __init__(self):
        # Initialize database
        self.engine = create_engine('sqlite:///inventory.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def add_product(self, name, quantity, price, category):
        product = Product(
            name=name,
            quantity=quantity,
            price=price,
            category=category
        )
        self.session.add(product)
        self.session.commit()
    
    def update_product(self, product_id, **kwargs):
        product = self.session.query(Product).filter_by(id=product_id).first()
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            product.last_updated = datetime.now()
            self.session.commit()
    
    def delete_product(self, product_id):
        product = self.session.query(Product).filter_by(id=product_id).first()
        if product:
            self.session.delete(product)
            self.session.commit()
    
    def get_all_products(self):
        return self.session.query(Product).all()
    
    def get_product(self, product_id):
        return self.session.query(Product).filter_by(id=product_id).first()

    def get_products_by_category(self):
        products = self.get_all_products()
        categories = {}
        for product in products:
            if product.category not in categories:
                categories[product.category] = []
            categories[product.category].append(product)
        return categories

class InventoryUI:
    def __init__(self):
        self.manager = InventoryManager()
        st.set_page_config(
            page_title="Inventory Management System",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        self.apply_custom_css()
    
    def apply_custom_css(self):
        st.markdown("""
        <style>
        .main {padding: 2rem;}
        .stButton>button {width: 100%; background-color: #4CAF50; color: white;}
        .stButton>button:hover {background-color: #45a049;}
        .stSelectbox {margin-bottom: 1rem;}
        .stForm {background-color: #f8f9fa; padding: 2rem; border-radius: 10px;}
        h1 {color: #2c3e50;}
        h2 {color: #34495e; margin-bottom: 1.5rem;}
        .row-widget.stButton button:nth-child(2) {background-color: #dc3545;}
        .row-widget.stButton button:nth-child(2):hover {background-color: #c82333;}
        </style>
        """, unsafe_allow_html=True)
    
    def main(self):
        st.title("📦 Inventory Management System")
        
        st.sidebar.image("https://img.icons8.com/color/96/000000/warehouse.png", width=100)
        st.sidebar.title("Navigation")
        menu = {
            "View Inventory": "📊",
            "Add Product": "➕",
            "Update Product": "🔄",
            "Delete Product": "🗑️"
        }
        choice = st.sidebar.selectbox(
            "Select Operation",
            list(menu.keys()),
            format_func=lambda x: f"{menu[x]} {x}"
        )
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        ### Quick Stats
        """)
        products = self.manager.get_all_products()
        total_products = len(products)
        total_value = sum(p.price * p.quantity for p in products)
        total_categories = len(set(p.category for p in products))
        
        col1, col2, col3 = st.sidebar.columns(3)
        col1.metric("Products", total_products)
        col2.metric("Value", f"${total_value:,.2f}")
        col3.metric("Categories", total_categories)
        
        if choice == "View Inventory":
            self.view_inventory()
        elif choice == "Add Product":
            self.add_product_form()
        elif choice == "Update Product":
            self.update_product_form()
        elif choice == "Delete Product":
            self.delete_product_form()
    
    def view_inventory(self):
        st.header("📊 Current Inventory")
        products = self.manager.get_all_products()
        if products:
            # Add search and filter options
            col1, col2 = st.columns(2)
            with col1:
                search = st.text_input("🔍 Search products", "")
            with col2:
                categories = list(set(p.category for p in products))
                selected_category = st.selectbox("📁 Filter by category", ["All"] + categories)
            
            data = [{
                'ID': p.id,
                'Name': p.name,
                'Quantity': p.quantity,
                'Price': f"${p.price:,.2f}",
                'Total Value': f"${p.price * p.quantity:,.2f}",
                'Category': p.category,
                'Last Updated': p.last_updated.strftime("%Y-%m-%d %H:%M")
            } for p in products
            if (search.lower() in p.name.lower() or search.lower() in p.category.lower()) and
               (selected_category == "All" or selected_category == p.category)]
            
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True)
                
                # Show category-wise summary
                st.subheader("📈 Category Summary")
                categories = self.manager.get_products_by_category()
                cols = st.columns(len(categories))
                for idx, (category, products) in enumerate(categories.items()):
                    with cols[idx]:
                        total_value = sum(p.price * p.quantity for p in products)
                        st.metric(
                            category or "Uncategorized",
                            f"${total_value:,.2f}",
                            f"{len(products)} items"
                        )
            else:
                st.warning("No products match your search criteria")
        else:
            st.info("🔍 No products in inventory")
    
    def add_product_form(self):
        st.header("➕ Add New Product")
        with st.form("add_product"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Product Name")
                quantity = st.number_input("Quantity", min_value=0)
            with col2:
                price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
                category = st.text_input("Category")
            
            submit = st.form_submit_button("Add Product")
            if submit:
                if name and price:
                    self.manager.add_product(name, quantity, price, category)
                    st.success("✅ Product added successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields")
    
    def update_product_form(self):
        st.header("🔄 Update Product")
        products = self.manager.get_all_products()
        if products:
            product_names = {f"{p.id}: {p.name}": p.id for p in products}
            selected_product = st.selectbox(
                "Select Product to Update",
                list(product_names.keys())
            )
            product_id = product_names[selected_product]
            
            product = self.manager.get_product(product_id)
            if product:
                with st.form("update_product"):
                    col1, col2 = st.columns(2)
                    with col1:
                        name = st.text_input("Product Name", value=product.name)
                        quantity = st.number_input("Quantity", value=product.quantity, min_value=0)
                    with col2:
                        price = st.number_input("Price ($)", value=product.price, min_value=0.0, format="%.2f")
                        category = st.text_input("Category", value=product.category)
                    
                    if st.form_submit_button("Update Product"):
                        self.manager.update_product(
                            product_id,
                            name=name,
                            quantity=quantity,
                            price=price,
                            category=category
                        )
                        st.success("✅ Product updated successfully!")
        else:
            st.info("ℹ️ No products available to update")
    
    def delete_product_form(self):
        st.header("🗑️ Delete Product")
        products = self.manager.get_all_products()
        if products:
            product_names = {f"{p.id}: {p.name}": p.id for p in products}
            selected_product = st.selectbox(
                "Select Product to Delete",
                list(product_names.keys())
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Delete Product", key="delete_btn"):
                    product_id = product_names[selected_product]
                    self.manager.delete_product(product_id)
                    st.success("✅ Product deleted successfully!")
            with col2:
                if st.button("Cancel", key="cancel_btn"):
                    st.stop()
        else:
            st.info("ℹ️ No products available to delete")

if __name__ == "__main__":
    app = InventoryUI()
    app.main()