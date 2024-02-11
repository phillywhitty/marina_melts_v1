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

