"""Custom template filters"""

from django import template

register = template.Library()

@register.filter(name="addClass")
def addClass(value, arg):
	"""Adds a css class to whatever django tag was input"""
	return value.as_widget(attrs={'class': arg})