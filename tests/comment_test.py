import unittest
from ..models import Comment,Pitch


class TestComment(unittest.TestCase):
    def setup(self):
        self.pitch = Pitch(pitch='we only live once', pitch_category='sales pitch')
        self.comment = Comment(comment='i like it',pitch = self.pitch)

    def test_comment_instance(self):
        self.assertEquals(self.comment.comment,'ilke it')
        self.assertEquals(self.comment.pitch,self.pitch)

    def test_save(self):
        self.comment.save_comment()
        self.assertTrue(len(Comment >0))  
        
    def test_get_comment(self):
        self.comment.save_comment()
        get=Comment.get_comments(self.pitch.id)
        self.assertTrue(len(get)==1)    