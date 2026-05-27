from selenium.webdriver.common.by import By

class RegistrationPage:

    #Форма регистрации:
    REGISTRATION_FORM = (By.TAG_NAME, 'form')

    #Заголовок формы:
    REGISTRATION_HEADER = (By.XPATH, '//main/div/h2')

    #Поле Имя:
    INPUT_NAME = (By.XPATH, '//form/fieldset[1]//input')
    #Поле Email:
    INPUT_EMAIL = (By.XPATH, '//form/fieldset[2]//input')
    #Поле Пароль:
    INPUT_PASSWORD = (By.XPATH, '//form/fieldset[3]//input')

    #Кнопка регистрации:
    REGISTRATION_BUTTON = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Зарегистрироваться"]')

    #Кнопка авторизации:
    AUTHORIZATION_BUTTON = (By.XPATH, '//div/p/a[text()="Войти"]')

    #Ошибка валидации пароля, текст:
    ERROR_TEXT = (By.XPATH, '//form/fieldset[3]//p')

class AuthorizationPage:

    #Кнопка авторизации на главном экране:
    AUTHORIZATION_BUTTON_MAIN = (By.XPATH, '//section[2]/div/button')

    #Форма авторизации:
    AUTHORIZATION_FORM = (By.TAG_NAME, 'form')

    #Поле Email:
    INPUT_EMAIL = (By.XPATH, '//form/fieldset[1]//input')

    #Поле Пароль:
    INPUT_PASSWORD = (By.XPATH, '//form/fieldset[2]//input')

    #Кнопка авторизации:
    AUTHORIZATION_BUTTON = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Войти"]')

    RECOVERY_BUTTON = (By.XPATH, '//div/p[2]/a[text()="Восстановить пароль"]')

class MainPage:

    #Кнопка оформления заказа
    BUTTON_ORDER = (By.XPATH, '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]//button[text()="Оформить заказ"]')

    #Кнопка перехода в личный кабинет
    BUTTON_ACCOUNT = (By.XPATH, '//header/nav/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]')

class RecoveryPasswordPage:

    #Форма восстановления пароля:
    RECOVERY_FORM = (By.TAG_NAME, 'form')

    #Кнопка перехода на страницу авторизации:
    BUTTON_TRANSITION = (By.XPATH, '//div/p/a[@class="Auth_link__1fOlj" and text()="Войти"]')

class PersonalAccountPage:

    #Раздел профиль активный:
    PROFILE_SECTION_ACTIVE = (By.XPATH, '//a[contains(@href, "/account/order-history")]')

    #Кнопка перехода в конструктор:
    BUTTON_CONSTRUCTION_INACTIVE = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]')

    #Кнопка выхода из аккаунта:
    BUTTON_LOG_OUT = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')

class Construction:

    #Раздел Булки неактивен:
    BUNS_SECTION_INACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]')

    #Раздел Булки активен:
    BUNS_SECTION_ACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]')

    #Раздел Соусы неактивен:
    SAUCES_SECTION_INACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]')

    #Раздел Соусы активен:
    SAUCES_SECTION_ACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]')

    #Раздел Начинки неактивен:
    TOPPINGS_SECTION_INACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]')

    #Раздел Начинки активен:
    TOPPINGS_SECTION_ACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]')


