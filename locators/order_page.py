order_page_url = 'https://stellarburgers.nomoreparties.site/' # URL Консруктор
order_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']" # Кнопка оформить заказ
selector_sauce = ".//span[text() = 'Соусы']" # Кнопка перехода к разделу Соусов
selector_fillings = ".//span[text() = 'Начинки']" # Кнопка перехода к разделу Начинки
selector_buns = ".//span[text() = 'Булки']" # Кнопка перехода к разделу Булки
parent_suace = ".//span[text() = 'Соусы']/parent::div" # Кнопка перехода к разделу Соусы, подвязка для ассерта
parent_fillings = ".//span[text() = 'Начинки']/parent::div" # Кнопка перехода к разделу Начинки, подвязка для ассерта
parent_buns = ".//span[text() = 'Булки']/parent::div" # Кнопка перехода к разделу Булки, подвязка для ассерта