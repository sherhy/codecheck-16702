#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib

def main(argv):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
	conn = httplib.HTTPConnection("http://challenge-server.code-check.io", 80)
	# conn.request("GET", "/api/hash")
	# conn.request("GET", "/api/hash?q=hoge")
	for i, v in enumerate(argv):
		conn.request("GET", "/api/hash?q="+v)
		response = conn.getresponse()

		print response.read()