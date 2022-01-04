#!/bin/bash
datatime_now=`date "+%Y-%m-%d %H:%M"`
git config --global user.name "SergeyL-1979"
git config --global user.email "SergeyLevchuk-1979"
git add *
git commit -m "$datatime_now"
git branch -M main
git remote add origin git@github.com:SergeyL-1979/NewsPortal_SK_D.git
git push -u origin main
