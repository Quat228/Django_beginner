from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)  # max_length обязателен для CharField
    pub_date = models.DateTimeField(auto_now=True)  # auto_now записывает время при записи данных

    def __str__(self):
        return f"Вопрос: {self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Вопрос #{self.question.id}, ответ: {self.choice_text}"

# models.CASCADE - удалиет все связанные данные
# on_delete поведение при удалении
