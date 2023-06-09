from main.models import Fridge


def assign_characteristics(model: Fridge, chartx):
    meta = model.fields_verbose
    for k in meta:
        for i in chartx:
            if meta[k] == i[:-1]:
                setattr(model, k, chartx[i])
                model.save()

    # for f in meta:
    #     model._meta.get_field(f).verbose_name.title()


# assign_characteristics(Fridge.objects.get(id=251), {'Общий объем:': '346 л', 'Объем холодильной камеры:': '241 л', 'Объем '
#                                                                                                               'морозильной камеры:': '105 л', 'Вес:': '67 кг', 'Высота:': '190 см', 'Глубина:': '65 см', 'Ширина:': '59.5 см', 'Габариты (ВхГхШ):': '190х65х59,5 см', 'Климатический класс:': 'ST', 'Количество камер:': '2 шт', 'Инверторный:': 'нет', 'Материал покрытия:': 'металл', 'Материал полок:': 'стекло', 'Тип управления:': 'электронный', 'Антибактериальное покрытие:': 'нет', 'Генератор льда:': 'нет', 'Защита от детей:': 'да', 'Режим "Отпуск":': 'да', 'Индикация открытой двери:': 'да', 'Индикация повышения температуры:': 'да', 'Особенности:': 'складная полка, LED-подсветка', 'Гарантия:': '12 мес', 'Изготовитель:': 'Россия', 'Размораживание морозильной камеры:': 'автоматическое', 'Хладагент:': 'R600a', 'Мощность замораживания:': '12 кг/сут', 'Индикация температуры:': 'да', 'Зона свежести:': 'нет', 'Класс энергопотребления:': 'A', 'Энергопотребление:': '360 кВтч/год', 'Уровень шума:': '39 дБ'})
