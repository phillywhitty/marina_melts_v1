Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [User Story Testing](#user-story-testing)
- [Stripe](#stripe)

## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Index |![index](./assets/testing/html/index_html_checker.png) | <mark>PASS<mark> |
| All products |![products](./assets/testing/html/products_page_html_checker.png) | <mark>PASS<mark> |
| Products Detail|![products_detail](./assets/testing/html/products_detail_html_chekcer.png) | <mark>PASS<mark> |
| Sign Up |![sign_up](./assets/testing/html/sign_up_html_checker.png) | <mark>PASS<mark> |
| Log In |![log_in](./assets/testing/html/log_in_html_checker.png) | <mark>PASS<mark> |
| My Profile |![my_profile](./assets/testing/html/my_profile_html_checker.png) | <mark>PASS<mark> |
| My Wallet |![wallet](./assets/testing/html/my_wallet_html_checker.png) | <mark>PASS<mark> |
| Checkout |![checkout](./assets/testing/html/checkout_html_checker.png) | <mark>PASS<mark> |
| Checkout Success |![checkout_success](./assets/testing/html/checkout_success_html_checker.png) | <mark>PASS<mark> |
| Log Out |![log_out](./assets/testing/html/log_out_html_checker.png) | <mark>PASS<mark> |
| Reset Password|![reset_password](/assets/testing/html/password_reset_html_checker.png) | <mark>PASS<mark> |
| Shopping Bag Empty |![shopping_bag_empty](./assets/testing/html/shopping_bag_empty_html_checker.png) | <mark>PASS<mark> |

### CSS
|file|Validator|Result|
| --- | --- | --- |
| base.css |![style](./assets/testing/css/base_css_css_checker.png) | <mark>PASS<mark> |
| checkout.css |![style](./assets/testing/css/checkout_css_checker.png) | <mark>PASS<mark> |

## JavaScript
|file|Validator|Result|Comment|
| --- | --- | --- |----|
| index page |![js](./assets/testing/js/index_js_checker.png) | <mark>PASS<mark> |This is mailchimp js script. It has 2 warnings and 3 undefined variables|
| products.js |![js](./assets/testing/js/products_js_checker.png) | <mark>PASS<mark> ||
| profile.js |![js](./assets/testing/js/profiles_js_checker.png) | <mark>PASS<mark> |This is js script from CI's walkthrough. I did not want to change this as the function is working. It has two warnings and shows $ as undefined variable |
| stripe.js |![js](./assets/testing/js/stripe_js_checker.png) | <mark>PASS<mark> |This is stripe.js. I did also not want to change this as the function works perfect. It has two warnings and two undefined variables inlcuding $ & stripe |

## Python

|File|App|Image|Result|Comment|
| --- |----| --- | --- |----|
| urls | wexford_treasures |![python](./assets/testing/python/wexford_treasures_main_urls_pep8.png) | <mark>PASS<mark> ||
| admin | profiles |![python](./assets/testing/python/profiles_admin_pep8.png) | <mark>PASS<mark> ||
| apps | profiles |![python](./assets/testing/python/profile_apps_pep8.png) | <mark>PASS<mark> ||
| forms | profiles |![python](./assets/testing/python/profiles_forms_pep8.png) | <mark>PASS<mark> ||
| models | profiles |![python](./assets/testing/python/profiles_models_pep8.png) | <mark>PASS<mark> ||
| urls | profiles |![python](./assets/testing/python/profiles_urls_pep8.png) | <mark>PASS<mark> ||
| views | profiles |![python](./assets/testing/python/profiles_views_pep8.png) | <mark>PASS<mark> ||
| admin | products |![python](./assets/testing/python/products_admin_pep8.png) | <mark>PASS<mark> ||
| apps | products |![python](./assets/testing/python/products_apps_pep8.png) | <mark>PASS<mark> ||
| forms | products |![python](./assets/testing/python/products_forms_pep8.png) | <mark>PASS<mark> ||
| models | products |![python](./assets/testing/python/products_models_pep8.png) | <mark>PASS<mark> ||
| urls | products |![python](./assets/testing/python/products_urls_pep8.png) | <mark>PASS<mark> ||
| views | products |![python](./assets/testing/python/products_views_pep8.png) | <mark>PASS<mark> ||
| widgets | products |![python](/assets/testing/python/products_widgets_pep8.png) | <mark>PASS<mark> ||
| apps | home |![python](./assets/testing/python/home_apps-pep8.png) | <mark>PASS<mark> ||
| urls | home |![python](./assets/testing/python/home_urls_pep8.png) | <mark>PASS<mark> ||
| views | home |![python](./assets/testing/python/home_views_pep8.png) | <mark>PASS<mark> ||
| test | home |![python](./assets/readme-images/testing/python/home-tests.PNG) | <mark>PASS<mark> ||
| urls | home |![python](./assets/readme-images/testing/python/home-urls.PNG) | <mark>PASS<mark> ||
| views | home |![python](./assets/readme-images/testing/python/home-views.PNG) | <mark>PASS<mark> ||
| admin | checkout |![python](./assets/testing/python/checkout_admin_pep8.png )| <mark>PASS<mark> ||
| apps | checkout |![python](./assets/testing/python/checkout_apps_pep8.png )| <mark>PASS<mark> ||
| forms | checkout |![python](./assets/testing/python/checkout_forms_pep8.png )| <mark>PASS<mark> ||
| models | checkout |![python](./assets/testing/python/checkout_models_pep8.png )| <mark>PASS<mark> ||
| signals | checkout |![python](./assets/testing/python/checkout_signals_pep8.png )| <mark>PASS<mark> ||
| urls | checkout |![python](./assets/testing/python/checkout_urls_pep8.png )| <mark>PASS<mark> ||
| views | checkout |![python](./assets/testing/python/checkout_views_pep8.png)| <mark>PASS<mark> ||
| webhook_handler | checkout |![python](./assets/testing/python/checkout_webhook_handler_pep8.png )| <mark>PASS<mark> ||
| webhooks | checkout |![python](./assets/testing/python/checkout_webhook_pep8.png )| <mark>PASS<mark> | This was Stripes webhook and I didnt want to change anything|
| apps | bag |![python](./assets/testing/python/bag_apps_pep8.png )| <mark>PASS<mark> ||
| context | bag |![python](./assets/testing/python/bag_context_pep8.png )| <mark>PASS<mark> ||
| urls | bag |![python](./assets/testing/python/bag_urls_pep8.png )| <mark>PASS<mark> ||
| views | bag |![python](./assets/testing/python/bag_views_pep8.png )| <mark>PASS<mark> ||


## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | ---|

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](./assets/testing/lighthouse/home_desktop_lighthouse.png) | <mark>PASS<mark> |
| Log-In Desktop |![home](./assets/testing/lighthouse/log_in_desktop_lighthouse.png) | <mark>PASS<mark> |
| Log-Out Desktop |![home](./assets/testing/lighthouse/log_out_desktop_lighthouse.png) | <mark>PASS<mark> |
| My Wallet Desktop |![home](./assets/testing/lighthouse/my_wallet_desktop_lighthouse.png) | <mark>PASS<mark> |
| Products Desktop |![home](./assets/testing/lighthouse/products_desktop_lighthouse.png) | <mark>PASS<mark> |
| Profile Desktop |![home](./assets/testing/lighthouse/profile_desktop_lighthouse.png) | <mark>PASS<mark> |
| Shopping Bag Desktop |![home](./assets/testing/lighthouse/shopping_bag_desktop_lighthouse.png) | <mark>PASS<mark> |

|User Story|Screenshot|Result|
| --- | --- | --- |
| As a shopper I can view a list of products so I can select some to purchase |![feature](./assets/testing/userstories/products_user_stories.png)| <mark>PASS<mark> |
| As a shopper I will see display details for a specific product so that I can identify the price, description, product rating, product image and available sizes |![feature](./assets/testing/userstories/products_detail_userstories.png)| <mark>PASS<mark> |
| As a shopper, I aim to swiftly spot discounts, clearance items, and special offers, enabling me to capitalize on exclusive savings for the products I intend to buy. |![feature](./assets/testing/userstories/deals_userstories.png)| <mark>PASS<mark> |
| As a shopper, I can effortlessly check the overall cost of my purchases to assist in preventing excessive spending |![feature](./assets/testing/userstories/bag_toast_userstories.png)| <mark>PASS<mark> |
| As a site user, I can conveniently sign up for an account and possess a personal profile, enabling me to view my account details |![feature](./assets/testing/userstories/my_profile_userstories.png)| <mark>PASS<mark> |
|As a site user, I can effortlessly log in or log out and gain access to my personal account information |![feature](./assets/testing/userstories/log_in_log_out_userstories.png)| <mark>PASS<mark> |
|As a site user, I can conveniently reset my password in case of forgetfulness, ensuring the recovery of access to my account |![feature](/assets/testing/userstories/password_reset_userstories.png)| <mark>PASS<mark> |
| As a site user, I aim to possess a customized user profile for viewing my individual order history, order confirmations, and the option to save my payment information![feature](./assets/readme-images/pagination.PNG)| <mark>PASS<mark> |
|As a an authenticated user I want to be able to add a review for a book product so that I can share my feedback and experiences with other potential buyers |![feature](./assets/readme-images/reviews.PNG)| <mark>PASS<mark> |
|As a user I want to be able to register an account so that I can have access to all functionality of BookHeaven. |![feature](./assets/readme-images/sign-up.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to log in to my account so that I can access my personalized features and make purchases on BookHeaven. |![feature](./assets/readme-images/sign-in.PNG)| <mark>PASS<mark> |
|As a registered user I want to be able to reset my password so that I can regain access to my account in case I forget my password |![feature](./assets/readme-images/password-reset.PNG)| <mark>PASS<mark> |
|As a registered user I want to be able to see my profile page so that I can update my information |![feature](./assets/readme-images/features/profile.PNG)| <mark>PASS<mark> |
|As a authenticated user, I want to be able to save books to my wishlist so that I can revisit and consider purchasing them later on BookHeaven. |![feature](./assets/readme-images/features/my-wishlist.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to add products to my shopping cart so that I can conveniently review and purchase multiple items at once on BookHeaven. |![feature](./assets/readme-images/features/card.png)| <mark>PASS<mark> |
|As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase on BookHeaven. |![feature](./assets/readme-images/cart-remove.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to adjust the quantity of products in my shopping cart so that I can control the quantity of items I want to purchase on BookHeaven. |![feature](./assets/readme-images/cart-remove.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to apply discount codes to my orders so that I can enjoy savings and discounts on my purchases at BookHeaven. |![feature](./assets/readme-images/discount_code.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases on BookHeaven with confidence. |![feature](./assets/readme-images/stripeintegration.PNG)| <mark>PASS<mark> |
|As an administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders made on BookHeaven. |![feature](./assets/readme-images/features/admin-dashboard.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to add new products to the website so that I can expand the product catalog on BookHeaven. |![feature](./assets/readme-images/features/add-product.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to remove products from the website so that I can manage the product catalog on BookHeaven. |![feature](./assets/readme-images/features/delete-product-confirmation.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to edit existing products on the website so that I can update and manage the product catalog on BookHeaven. |![feature](./assets/readme-images/features/edit-product.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to edit the stock levels of products so that I can manage inventory and ensure product availability on BookHeaven. |![feature](./assets/readme-images/features/edit-product.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to submit a testimonial about my overall experience with the website so that I can provide feedback and share my positive experiences on BookHeaven. || Won't Have |
|As a user, I want to be able to view testimonials submitted by other users so that I can read about the experiences and feedback of fellow users on BookHeaven. || Won't Have |
|As a website owner, I want to improve the website's search engine optimization (SEO) so that the website can rank higher in search engine results and attract more organic traffic.  |Descriptive meta tags were added to the main template, including title, description and keywords. A sitemap was generated using xml-sitemaps This was generated using the deployed website. The file is included in the root level of the project. Robots.txt file was created at the root level of the project. This file tells the search engine crawlers which URLs they can access on the website.| <mark>PASS<mark> |
|As a user, I want to sign up for newsletters on the website so that I can keep up with updates and deals. |![feature](./assets/readme-images/features/newsletter.PNG)| <mark>PASS<mark> |
|As a user I want to be able to sort the list of available products by name and price so that I can easily find books that match my interests |![feature](./assets/readme-images/product-sort.PNG)| <mark>PASS<mark> |
|As a User I want to be able to complete the checkout process for my shopping cart so that I can purchase the items I've added to my cart |![feature](./assets/readme-images/checkout.PNG)| <mark>PASS<mark> |
|As a an authenticated user I want to be able to delete my reviews for a book product so that I can manage and maintain the accuracy and relevance of my feedback |![feature](./assets/readme-images/delete-review.PNG)| <mark>PASS<mark> |
|As a an authenticated user I want to be able to edit my reviews for a book product so that I can manage and maintain the accuracy and relevance of my feedback |![feature](./assets/readme-images/edit-review.PNG)| <mark>PASS<mark> |