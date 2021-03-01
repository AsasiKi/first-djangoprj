from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #admin계정에 생성한 걸 그대로 쓰겠다는 로직
    #on delete는 연동된 로직을 같이 지우겠다는 로직
    title = models.CharField(max_length=200) 
    #글자 수 제한이 있는 로직
    text=models.TextField()
    #글자 수 제한이 없는 로직
    created_datae= models.DateTimeField(default=timezone.now) 
    # 공개한 서버 시간 저장할 로직 timezone.now
    published_date = models.DateTimeField(blank=True, null=True) 
    # blank=True일 경우 컬럼이 비어있어도 됨, null=True는 null값을 넣기 허용
    # title text의 경우 blank가 없으니 무조건 입력 값을 넣어야 함

    def publish(self):
        self.publised_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title
    