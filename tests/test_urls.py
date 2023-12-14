import pytest
from django.test import client
from django.core.management import call_command
from django.urls import resolve
from django.contrib.admin import AdminSite

# 正しく、admin.site.urls が呼び出されていることを確認するテスト
def test_can_access_top_page():
    view = resolve('/admin/')
    assert view.func.__module__ == 'django.contrib.admin.sites'
    assert view.func.__name__ == 'index'