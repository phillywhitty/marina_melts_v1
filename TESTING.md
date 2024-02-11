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
|As a site user, I aim to possess a customized user profile for viewing my individual order history, order confirmations, and the option to save my payment information |![feature](./assets/testing/userstories/order_history_userstories.png)| <mark>PASS<mark> |
|As a shopper, I would like the ability to arrange a list of products, making it effortless to pinpoint the top-rated, most reasonably priced, and categorically sorted items |![feature](/assets/testing/userstories/sort_bar_userstories.png)| <mark>PASS<mark> |
|As a shopper, I aim to have the capability to simultaneously sort multiple categories of products, facilitating the discovery of the best-priced or top-rated items across broad categories like hampers or gift sets |![feature](./assets/testing/userstories/best_price_userstories.png)| <mark>PASS<mark> |
|As a shopper, I desire the capability to search for a product by its name or description, allowing me to locate and purchase a specific item |![feature](./assets/testing/userstories/search_bar_userstories.png)| <mark>PASS<mark> |
|As a shopper, I wish to quickly view my search results and the count, enabling me to promptly determine if the desired product is available |![feature](./assets/testing/userstories/product_available_userstories.png)| <mark>PASS<mark> |
|As a shopper, I desire the ability to inspect the items in my shopping bag before making a purchase, allowing me to identify the total cost of my order and review all the items I will receive. |![feature](./assets/testing/userstories/shopping_bag_userstories.png)| <mark>PASS<mark> |
|As a shopper, I aim to effortlessly input my payment information, ensuring a quick and hassle-free checkout process |![feature](./assets/testing/userstories/checkout_card_details_userstories.png)| <mark>PASS<mark> |
|As a shopper, I aim to have the option to review an order confirmation after checkout, ensuring that I have not made any mistakes in my purchase |![feature](./assets/testing/userstories/order_confirmation_userstories.png)| <mark>PASS<mark> |
|As a shopper, I desire to receive an email confirmation after completing the checkout process to retain a record of my purchase for my personal records |![feature](./assets/testing/userstories/email_confirmation_userstories.png)| <mark>PASS<mark> |
|As a store owner, I wish to include a new product, allowing me to update my store with new items |![feature](./assets/testing/userstories/product_add_userstories.png)| <mark>PASS<mark> |

