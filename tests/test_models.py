# -*- coding: utf-8 -*-
import pytest
pytestmark = pytest.mark.django_db


import django_dirty
from .models import Post


def test_dirty():
    post = Post.objects.create(title='Django', tag=10)

    assert post._original.tag == 10

    post.tag = 20

    assert post._original.tag == 10
