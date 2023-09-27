from django.db import models


class Slidemainpage(models.Model):
    title = models.CharField('название', max_length=160)
    slhead = models.CharField('заголовок слайдера', max_length=60)
    slp = models.TextField('параграф слайдера')
    slimage = models.ImageField(upload_to='static/main/images/banner/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Главный слайдер'
        verbose_name_plural='Слайды главной страницы'

class Aboutus(models.Model):
    header = models.CharField('Заголовок', max_length=100)
    text = models.TextField('текст')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name='текст О НАС'
        #verbose_name_plural='Слайды главной страницы'

class Quest(models.Model):
    question = models.CharField('Вопрос', max_length=160)
    answer = models.TextField('Ответ')
    #uniq = models.CharField('юник', max_length=10)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name='Вопрос-ответ'
        verbose_name_plural='Вопросы и ответы'


class Prices(models.Model):
    cost = models.CharField('стоимость', max_length=6)
    description = models.CharField('описание', max_length=20)
    yellow = models.BooleanField('Жёлтый', default='none')
    title = models.CharField('Программа', default='АКПП', max_length=15)


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Соимость'
        verbose_name_plural = 'Цена'