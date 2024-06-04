registration_page_url = "https://stellarburgers.nomoreparties.site/register" # XPATH URL страницы регистрации
registration_name_input = ".//label[text()='Имя']/parent::div/input" # XPATH Инпут поля Имя
registration_email_input = ".//label[text()='Email']/parent::div/input" # XPATH Инпут поля email
registration_password_input = ".//label[text()='Пароль']/parent::div/input" # XPATH Инпут поля Пароль
registration_wrong_password = ".//div/main/div/form/fieldset[3]/div/p[text()='Некорректный пароль']" # XPATH Текст ошибки о некорректном пароле
registration_registr_button = ".//div/main/div/form/button[text()='Зарегистрироваться']" # XPATH Кнопка регистрации
registration_login_button = "Войти" # LINK_TEXT Кнопка "Войти" на странице регистрации