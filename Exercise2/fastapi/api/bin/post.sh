#!/bin/sh

http --verbose POST localhost:5200/api/books/ @"$1"
