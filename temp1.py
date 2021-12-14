class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name        
        self.year_birth = year_birth        
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())

# Создайте экземпляр класса Contact с необходимыми параметрами
# Например, test_old_none_programmer = Contact('Пушкин', 1799, False).
# Напишите assert, и в нём проверьте, 
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный"
# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина"

# Затем создайте другой экземпляр с другими параметрами
# И в assert проверьте, вернут ли и его методы ожидаемый результат.

# Создайте столько экземпляров, сколько нужно, 
# чтобы через разные assert проверить все методы во всех вариантах.

first_contact = Contact('Pol', 1799, False)
assert first_contact.age_define() == 'Старейшина', 'Error!'
assert first_contact.programmer_define() == 'Нормальный', 'Error!'
assert first_contact.show_contact() == 'Pol, возраст: Старейшина, статус: Нормальный', 'Error!'

second_contact = Contact('Ven', 1960, True)
assert second_contact.age_define() == 'Олдскул', 'Error!'
assert second_contact.programmer_define() == 'Программист', 'Error!'

third_contact = Contact('Kris', 2000, True)
assert third_contact.age_define() == 'Молодой', 'Error!'
assert third_contact.programmer_define() == 'Программист', 'Error!'


