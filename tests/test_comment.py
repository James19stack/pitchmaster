import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):
    def setup(self):
        self.user_james = User(username = 'James',password = 'jefferson')
        self.comment = Comment(comment='i like it',user = self.user_James)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.comment.comment,'i like it')
        self.assertEquals(self.comment.user,self.user_James)

    def test_save_comment(self):
        self.comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.comment.save_comment()
        get = Comment.get_comments(self.pitch.id)
        self.assertTrue(len(got_comments) == 1)