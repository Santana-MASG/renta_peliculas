from behave import given, when, then
import time
from selenium import webdriver
from unittest import TestCase


@given(u'Que ingreso logueado a la vista películas')
def step_impl(context):
    login(context)
    time.sleep(1)
    context.driver.get(context.url+'peliculas')


@given(u'selecciono una de las películas disponibles')
def step_impl(context):
    context.driver.get(context.url+'peliculas')
    context.driver.find_element_by_id('1').click()

@when(u'presiono el botón rentar')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id('rentar').click()


@then(u'puedo ver que el stock de la pelicula seleccionada disminuye')
def step_impl(context):
    time.sleep(1)
    context.driver.get(context.url+'peliculas')

def login(context):
    context.driver.get(context.url+'admin')
    context.driver.find_element_by_id('id_username').send_keys('santana')
    context.driver.find_element_by_id('id_password').send_keys('santana123')
    context.driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/form/div[3]/input').click()
