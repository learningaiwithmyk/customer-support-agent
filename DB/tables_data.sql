
--MySQL Scripts for Each Service:

--#1 Track your package :
INSERT INTO customer_support_agent.package_service
(user_id, contact_info, package_id, order_id, delivery_address, delivery_status, expected_delivery_date, notes, created_by, updated_by)
VALUES
(1, 'user1@example.com', 'PKG12345', 'ORD67890', '123 Main St, Springfield, IL', 'IN_TRANSIT', '2025-02-10', 'Handle with care', 'admin', 'admin'),
(2, 'user2@example.com', 'PKG67890', 'ORD12345', '456 Park Ave, New York, NY', 'DELIVERED', '2025-01-20', 'Left at the front porch', 'admin', 'admin');


--#2 Returns Policies
INSERT INTO customer_support_agent.policy_details
(type_of_policy, policy_product, policy_details, policy_validity_period, created_by, updated_by)
VALUES
('return_policy', 'electronics', 'Returns accepted within 30 days with receipt.', '2025-12-31', 'admin', 'admin'),
('return_policy', 'books', 'Books can be returned within 15 days if they are in new condition without any markings or damage.', '2025-12-31', 'admin', 'admin'),
('return_policy', 'food', 'Returns accepted only for unopened, non-perishable food items within 7 days of delivery.', '2025-08-31', 'admin', 'admin'),
('exchange_policy', 'clothing', 'Exchanges allowed within 15 days for unworn items.', '2025-06-30', 'admin', 'admin');


--#3 Product Info[Amazon Prime,Alexa]
INSERT INTO customer_support_agent.product_details
(product_type, product_name, product_description, process_to_buy, product_price, created_by, updated_by)
VALUES
('subscription', 'Amazon Prime', 'Fast delivery and streaming service.', 'Sign up on the Amazon website.', 129.99, 'admin', 'admin'),
('device', 'Alexa', 'Smart voice assistant for your home.', 'Order through Amazon.', 49.99, 'admin', 'admin');


--#4 Update Contact Info
INSERT INTO customer_support_agent.update_contact_info_details
(contact_type, way_of_update, contact_priority, created_by, updated_by)
VALUES
('email', 'Login to your account, go to Settings, and update the email.', 'primary', 'admin', 'admin'),
('phone', 'Login to your account, verify OTP, and update the phone number.', 'secondary', 'admin', 'admin');


--#5 Update Password
INSERT INTO customer_support_agent.login_support
(type_of_support, way_of_update, support_status, created_by, updated_by)
VALUES
('password_update', 'Click the "Forgot Password" link, verify OTP, and set a new password.', 'ACTIVE', 'admin', 'admin'),
('account_unlock', 'Contact customer support for account unlock.', 'INACTIVE', 'admin', 'admin');


