from django.db import models
from django.contrib.auth.models import User


class FileModel(models.Model):
    caption = models.CharField(max_length=100)
    file = models.FileField()
    board = models.ForeignKey("DocBoardModel", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Files"


class DocBoardModel(models.Model):

    CHOICE_HTML = "html"
    CHOICE_CSS = "css"
    CHOICE_JS = "javascript"
    CHOICE_ES6 = "es6"
    CHOICE_NODE = "node,js"
    CHOICE_JAVA = "java"
    CHOICE_PYTHON = "python"
    CHOICE_SQL = "sql"
    CHOICE_REACT = "react"
    CHOICE_RN = "react-native"
    CHOICE_FIREBASE = "firebase"
    CHOICE_UNITY = "unity"
    CHOICE_GRAPHQL = "graphql"

    CHOICE_TYPE = (
        (CHOICE_HTML, "html"),
        (CHOICE_CSS, "css"),
        (CHOICE_JS, "javascript"),
        (CHOICE_ES6, "es6"),
        (CHOICE_NODE, "node,js"),
        (CHOICE_JAVA, "java"),
        (CHOICE_PYTHON, "python"),
        (CHOICE_SQL, "sql"),
        (CHOICE_REACT, "react"),
        (CHOICE_RN, "react-native"),
        (CHOICE_FIREBASE, "firebase"),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    board_type = models.CharField(choices=CHOICE_TYPE, max_length=40)
    like_count = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def displayUser(self):
        return self.author.username

    displayUser.short_description = "author"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "DOC_BOARDS"
