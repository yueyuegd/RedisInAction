#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

ONE_WEEK_IN_SECOND = 7 * 86400
VOTE_SCORE = 432
def article_vote(conn, user, article) :
    cutoff = time.time() - ONE_WEEK_IN_SECOND
    if conn.zscore('time:', article) < cutoff:
        return
    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):
        conn.zincrby('voted:' + article_id, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)