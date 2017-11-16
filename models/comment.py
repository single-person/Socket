from models import Model
from models.user import User


class Comment(Model):
    """
    评论类
    """
    content: str
    # 和别的数据关联的方式, 用 user_id 表明拥有它的 user 实例
    user_id: int
    weibo_id: int

    def user(self):
        u : User = User.find_by(id=self.user_id)
        return u
