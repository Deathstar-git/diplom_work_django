from django.db import models
from django.db.models import CharField
from django.urls import reverse


class Fridge(models.Model):  # Холодильники
    title = models.TextField(blank=False, null=False, verbose_name='Название')
    img_url = models.TextField(null=True, blank=True, verbose_name='Ссылка на картинку')

    # Характеристики
    @property
    def fields(self):
        return [f.name for f in self._meta.fields + self._meta.many_to_many]

    def get_absolute_url(self):
        return reverse('fridge', kwargs={'_id': self.pk})

    @property
    def fields_verbose(self):
        return dict([(f.name, f.verbose_name) for f in self._meta.fields + self._meta.many_to_many])
    total_useful_volume = CharField(null=True, blank=True, max_length=100, verbose_name='Общий полезный обьем')
    total_volume = CharField(null=True, blank=True, max_length=100, verbose_name='Общий обьем')
    useful_volume_refrigerator = CharField(null=True, blank=True, max_length=100, verbose_name='Общий полезный '
                                                                                                 'обьем холодильной '
                                                                                                 'камеры')
    volume_refrigerator = CharField(null=True, blank=True, max_length=100, verbose_name='Общий обьем холодильной '
                                                                                          'камеры')
    volume_freezer = CharField(null=True, blank=True, max_length=100, verbose_name='Объем морозильной камеры')
    useful_volume_freezer = CharField(null=True, blank=True, max_length=100, verbose_name='Полезный объем '
                                                                                            'морозильной камеры')
    weight = CharField(null=True, blank=True, max_length=100, verbose_name='Вес')
    height = CharField(null=True, blank=True, max_length=100, verbose_name='Высота')
    width = CharField(null=True, blank=True, max_length=100, verbose_name='Ширина')
    depth = CharField(null=True, blank=True, max_length=100, verbose_name='Глубина')
    dimensions = CharField(null=True, blank=True, max_length=100, verbose_name='Габариты (ВхГхШ)')
    package_height = CharField(null=True, blank=True, max_length=100, verbose_name='Высота упаковки')
    package_width = CharField(null=True, blank=True, max_length=100, verbose_name='Ширина упаковки')
    package_length = CharField(null=True, blank=True, max_length=100, verbose_name='Длина упаковки')
    climate_class = CharField(null=True, blank=True, max_length=100, verbose_name='Климатический класс')
    count_coolstore = CharField(null=True, blank=True, max_length=100, verbose_name='Количество камер')
    control_type = CharField(null=True, blank=True, max_length=100, verbose_name='Тип управления')
    inverter = CharField(null=True, blank=True, max_length=100, verbose_name='Инверторный')
    coating_material = CharField(null=True, blank=True, max_length=100, verbose_name='Материал покрытия')
    shelf_material = CharField(null=True, blank=True, max_length=100, verbose_name='Материал полок')
    autonomous_cold_storage = CharField(null=True, blank=True, max_length=100, verbose_name='Автономное сохранение '
                                                                                            'холода')
    antibacterial_coating = CharField(null=True, blank=True, max_length=100, verbose_name='Антибактериальное покрытие')
    ice_maker = CharField(null=True, blank=True, max_length=100, verbose_name='Генератор льда')
    child_protection = CharField(null=True, blank=True, max_length=100, verbose_name='Защита от детей')
    power_failure_indicator = CharField(null=True, blank=True, max_length=100, verbose_name='Индикация отключения '
                                                                                            'электропитания')
    holiday_mode = CharField(null=True, blank=True, max_length=100, verbose_name='Режим "Отпуск"')
    open_door_indicator = CharField(null=True, blank=True, max_length=100, verbose_name='Индикация открытой двери')
    temperature_increase_indicator = CharField(null=True, blank=True, max_length=100, verbose_name='Индикация '
                                                                                                   'повышения '
                                                                                                   'температуры')
    peculiarities = CharField(null=True, blank=True, max_length=100, verbose_name='Особенности')
    guarantee = CharField(null=True, blank=True, max_length=100, verbose_name='Гарантия')
    manufacturer = CharField(null=True, blank=True, max_length=100, verbose_name='Изготовитель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Холодильник'
        verbose_name_plural = 'Холодильники'


class FridgeGrade(models.Model):
    negative_count = models.IntegerField(default=0)
    neutral_count = models.IntegerField(default=0)
    positive_count = models.IntegerField(default=0)
    total_grade = models.IntegerField(default=0)
    fridge = models.OneToOneField(Fridge, on_delete=models.CASCADE, primary_key=True)


class FridgeComment(models.Model):  # Комментарии
    text = models.TextField(null=True, blank=True, verbose_name='Содержание')
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(null=True)

    def __str__(self):
        return f'Комментарий #{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class MobilePhone(models.Model):  # Мобильные телефоны
    title = models.TextField(blank=False, null=False, verbose_name='Название')
    img_url = models.TextField(null=True, blank=True, verbose_name='Ссылка на картинку')

    @property
    def fields(self):
        return [f.name for f in self._meta.fields + self._meta.many_to_many]

    def get_absolute_url(self):
        return reverse('mobile_phone', kwargs={'_id': self.pk})

    @property
    def fields_verbose(self):
        return dict([(f.name, f.verbose_name) for f in self._meta.fields + self._meta.many_to_many])

    # Характеристики
    screen_matrix_type = CharField(null=True, blank=True, max_length=100, verbose_name='Тип матрицы экрана')
    screen_diagonal = CharField(null=True, blank=True, max_length=100, verbose_name='Диагональ экрана')
    touch_screen = CharField(null=True, blank=True, max_length=100, verbose_name='Сенсорный экран')
    camera = CharField(null=True, blank=True, max_length=100, verbose_name='Фотокамера')
    camera_resolution = CharField(null=True, blank=True, max_length=100, verbose_name='Разрешение фотокамеры')
    front_camera = CharField(null=True, blank=True, max_length=100, verbose_name='Фронтальная камера')
    battery_capacity = CharField(null=True, blank=True, max_length=100, verbose_name='Емкость аккумулятора')
    organizer_calendar = CharField(null=True, blank=True, max_length=100, verbose_name='Органайзер/календарь')
    computer_synchronization = CharField(null=True, blank=True, max_length=100, verbose_name='Синхронизация с компьютером')
    calculator = CharField(null=True, blank=True, max_length=100, verbose_name='Калькулятор')
    weight = CharField(null=True, blank=True, max_length=100, verbose_name='Вес')
    height = CharField(null=True, blank=True, max_length=100, verbose_name='Высота')
    thickness = CharField(null=True, blank=True, max_length=100, verbose_name='Толщина')
    width = CharField(null=True, blank=True, max_length=100, verbose_name='Ширина')
    talk_time = CharField(null=True, blank=True, max_length=100, verbose_name='Время разговора')
    builtin_memory = CharField(null=True, blank=True, max_length=100, verbose_name='Объем встроенной памяти')
    memory_card_slot = CharField(null=True, blank=True, max_length=100, verbose_name='Слот для карты памяти')
    memory_card_type = CharField(null=True, blank=True, max_length=100, verbose_name='Тип карты памяти')
    max_memory_card_size = CharField(null=True, blank=True, max_length=100, verbose_name='Максимальный объем карты памяти')
    gsm = CharField(null=True, blank=True, max_length=100, verbose_name='GSM')
    three_g_support = CharField(null=True, blank=True, max_length=100, verbose_name='Поддержка 3G (UMTS)')
    wi_fi = CharField(null=True, blank=True, max_length=100, verbose_name='Wi-Fi')
    bluetooth = CharField(null=True, blank=True, max_length=100, verbose_name='Стандарт Bluetooth')
    usb_interface = CharField(null=True, blank=True, max_length=100, verbose_name='Интерфейс USB')
    headphone_output = CharField(null=True, blank=True, max_length=100, verbose_name='Выход на наушники')
    sos = CharField(null=True, blank=True, max_length=100, verbose_name='Наличие кнопки SOS')
    manufacturer = CharField(null=True, blank=True, max_length=100, verbose_name='Изготовитель')
    guarantee = CharField(null=True, blank=True, max_length=100, verbose_name='Гарантия')
    peculiarities = CharField(null=True, blank=True, max_length=100, verbose_name='Объем встроенной памяти')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мобильный телефон'
        verbose_name_plural = 'Мобильные телефоны'


class MobilePhoneGrade(models.Model):
    negative_count = models.IntegerField(default=0)
    neutral_count = models.IntegerField(default=0)
    positive_count = models.IntegerField(default=0)
    total_grade = models.IntegerField(default=0)
    phone = models.OneToOneField(MobilePhone, on_delete=models.CASCADE, primary_key=True)


class MobilePhoneComment(models.Model):  # Комментарии
    text = models.TextField(null=True, blank=True, verbose_name='Содержание')
    phone = models.ForeignKey(MobilePhone, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(null=True)

    def __str__(self):
        return f'Комментарий #{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Multicooker(models.Model):  # Мультиварки
    title = models.TextField(blank=False, null=False, verbose_name='Название')
    img_url = models.TextField(null=True, blank=True, verbose_name='Ссылка на картинку')

    @property
    def fields(self):
        return [f.name for f in self._meta.fields + self._meta.many_to_many]

    def get_absolute_url(self):
        return reverse('multicooker', kwargs={'_id': self.pk})

    @property
    def fields_verbose(self):
        return dict([(f.name, f.verbose_name) for f in self._meta.fields + self._meta.many_to_many])

    # Характеристики
    type = CharField(null=True, blank=True, max_length=100, verbose_name='Тип')
    bowl_volume = CharField(null=True, blank=True, max_length=100, verbose_name='Объем чаши')
    control_type = CharField(null=True, blank=True, max_length=100, verbose_name='Тип управления')
    three_d_heating = CharField(null=True, blank=True, max_length=100, verbose_name='3D нагрев')
    housing_material = CharField(null=True, blank=True, max_length=100, verbose_name='Материал корпуса')
    bowl_cover = CharField(null=True, blank=True, max_length=100, verbose_name='Покрытие чаши')
    power_consumption = CharField(null=True, blank=True, max_length=100, verbose_name='Потребляемая мощность')
    delayed_start = CharField(null=True, blank=True, max_length=100, verbose_name='Отложенный старт')
    max_timer_setting_time = CharField(null=True, blank=True, max_length=100, verbose_name='Максимальное время установки таймера')
    keep_warm = CharField(null=True, blank=True, max_length=100, verbose_name='Поддержание тепла')
    color = CharField(null=True, blank=True, max_length=100, verbose_name='Цвет')
    guarantee = CharField(null=True, blank=True, max_length=100, verbose_name='Гарантия')
    viewing_window = CharField(null=True, blank=True, max_length=100, verbose_name='Смотровое окно')
    count_automatic_program = CharField(null=True, blank=True, max_length=100, verbose_name='Число автоматических программ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мультиварка'
        verbose_name_plural = 'Мультиварки'


class MulticookerGrade(models.Model):
    negative_count = models.IntegerField(default=0)
    neutral_count = models.IntegerField(default=0)
    positive_count = models.IntegerField(default=0)
    total_grade = models.IntegerField(default=0)
    multicooker = models.OneToOneField(Multicooker, on_delete=models.CASCADE, primary_key=True)


class MulticookerComment(models.Model):  # Комментарии
    text = models.TextField(null=True, blank=True, verbose_name='Содержание')
    multicooker = models.ForeignKey(Multicooker, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(null=True)

    def __str__(self):
        return f'Комментарий #{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'