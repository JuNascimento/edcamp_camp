# encoding: utf-8
from django.db import models
from django.utils import timezone

# Create your models here.

class Campeonato(models.Model):
	class Meta:
		verbose_name = "Campeonato"
		verbose_name_plural = "Campeonatos"
	
	
	campeonato_id = models.PositiveSmallIntegerField() #pkz
	nome = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	descricao = models.CharField(max_length=200)

	# @property
	# def campeonato_id(self):
	# 	return self.id

	def __str__(self):
		return self.nome

class Edicao(models.Model):
	class Meta:
		verbose_name = "Edição"
		verbose_name_plural = "Edições"

	edicao_id = models.PositiveSmallIntegerField() #pk
	Campeonato = models.ForeignKey('Campeonato') #fk
	nome = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)

	
	def __str__(self):
		return self.nome