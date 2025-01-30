
--MySQL Scripts for Each Service:

--#1 Track your package :
CREATE TABLE customer_support_agent.package_service (
    user_id INT,
    contact_info VARCHAR(255),
    package_id VARCHAR(100),
    order_id VARCHAR(100),
    delivery_address VARCHAR(255),
    delivery_status ENUM('IN_TRANSIT', 'DELIVERED', 'CANCELLED', 'FAILED'),
    expected_delivery_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by VARCHAR(100)
);


--#2 Returns Policies
CREATE TABLE customer_support_agent.policy_details (
               policy_id INT AUTO_INCREMENT PRIMARY KEY,
               type_of_policy ENUM('return_policy', 'exchange_policy', 'refund_policy'),
               policy_product ENUM('electronics', 'books', 'food', 'clothing'),
               policy_details TEXT,
               policy_validity_period DATE,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               created_by VARCHAR(100),
               updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
               updated_by VARCHAR(100)
);


--#3 Product Info[Amazon Prime,Alexa]
CREATE TABLE customer_support_agent.product_details (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_type ENUM('subscription', 'device', 'service'),
    product_name VARCHAR(255),
    product_description TEXT,
    process_to_buy TEXT,
    product_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by VARCHAR(100)
);


--#4 Update Contact Info
CREATE TABLE customer_support_agent.update_contact_info_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contact_type ENUM('email', 'phone'),
    way_of_update TEXT,
    contact_priority ENUM('primary', 'secondary'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by VARCHAR(100)
);


--#5 Update Password
CREATE TABLE customer_support_agent.login_support (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_of_support ENUM('password_update', 'account_unlock'),
    way_of_update TEXT,
    support_status ENUM('ACTIVE', 'INACTIVE'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by VARCHAR(100)
);

