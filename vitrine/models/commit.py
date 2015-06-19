#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of vitrine.
# https://github.com/globocom/vitrine

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Globo.com <talentos@corp.globo.com>

from vitrine.db import mongo


class Commit(mongo.Document):

    commit_id = mongo.StringField(max_length=50, unique=True)
    short_id = mongo.StringField(max_length=15)
    title = mongo.StringField(max_length=100)
    author_name = mongo.StringField(required=True)
    author_email = mongo.StringField(required=True)
    created_at = mongo.DateTimeField(required=True)
    owner = mongo.StringField(required=True)
    project_id = mongo.IntField()
    project_name = mongo.StringField(required=True)
    message = mongo.StringField()
