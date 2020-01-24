# Stata Extended 

by Linxiao Francis Cong

* Version: 0.0.0
* Date: 23 January 2020

## Introduction

This package contains functions to facilitate Stata coding, to be used together with [StataEditor](https://github.com/mattiasnordin/StataEditor). This is for personal use only. 

## Features

### Change substitution between local and global

In Stata, local and global names are referenced differently: `` `local'`` and `${global}` (or `$global`). Sometimes, you may want to change a local into a global. As a result, you have to change every occurrence of  `` `foo'`` into `${foo}`. Sometimes, you may also want to change a global in to a local. This package provides the following two shortcuts to do this:

* `Ctrl+g`: change from local to global;
* `Ctrl+Shift+l`: change from global to local;

I do not choose `Ctrl+Shift+g` or `Ctrl+l` since the former is inconvenient and the latter may be commonly used.

The usage is simple:

1. Select the (local or global) name that you want to change, e.g. `foo`. You can select multiple names.
2. If you press`Ctrl+g`,  all ```foo'`` will be changed to ``${foo}``; if you press ``Ctrl+Shift+l``, all ``${foo}`` will be changed to ``foo'` .

More features to be added later.