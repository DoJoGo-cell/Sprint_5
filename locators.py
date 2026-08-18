from selenium.webdriver.common.by import By

class RegistrationPage:

    #Форма регистрации:
    REGISTRATION_FORM = (By.CSS_SELECTOR, 'form')

    #Заголовок формы:
    REGISTRATION_HEADER = (By.XPATH, '//h2[text()="Регистрация"]')

    #Поле Имя:
    INPUT_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    #Поле Email:
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    #Поле Пароль:
    INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

    #Кнопка регистрации:
    REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    #Кнопка авторизации:
    AUTHORIZATION_BUTTON = (By.XPATH, '//a[text()="Войти"]')

    #Ошибка валидации пароля, текст:
    ERROR_TEXT_PASSWORS = (By.XPATH, '//p[text()="Некорректный пароль"]')


class AuthorizationPage:

    #Кнопка авторизации на главном экране:
    AUTHORIZATION_BUTTON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    #Форма авторизации:
    AUTHORIZATION_FORM = (By.CSS_SELECTOR, 'form')

    #Поле Email:
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    #Поле Пароль:
    INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

    #Кнопка авторизации:
    AUTHORIZATION_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    RECOVERY_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')

class MainPage:

    #Кнопка оформления заказа
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')

    #Кнопка перехода в личный кабинет
    BUTTON_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')

class RecoveryPasswordPage:

    #Форма восстановления пароля:
    RECOVERY_FORM = (By.CSS_SELECTOR, 'form')

    #Кнопка перехода на страницу авторизации:
    BUTTON_TRANSITION = (By.XPATH, '//p[text()="Вспомнили пароль?"]/a[text()="Войти"]')

class PersonalAccountPage:

    #Раздел профиль активный:
    PROFILE_SECTION_ACTIVE = (By.XPATH, '//a[@aria-current="page" and text()="Профиль"]')

    #Кнопка перехода в конструктор:
    BUTTON_CONSTRUCTION_INACTIVE = (By.XPATH, '//p[text()="Конструктор"]')

    #Кнопка выхода из аккаунта:
    BUTTON_LOG_OUT = (By.XPATH, '//button[text()="Выход"]')

class Construction:

    #Раздел Булки выбран:
    BUNS_SECTION_SELECTED = (By.XPATH, '//div[contains(@class, "current")]//span[text()="Булки"]')

    #Раздел Соусы:
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')

    #Раздел Соусы выбран:
    SAUCES_SECTION_SELECTED = (By.XPATH, '//div[contains(@class, "current")]//span[text()="Соусы"]')

    #Раздел Начинки:
    TOPPINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')

    #Раздел Начинки выбран:
    TOPPINGS_SECTION_SELECTED = (By.XPATH, '//div[contains(@class, "current")]//span[text()="Начинки"]')



