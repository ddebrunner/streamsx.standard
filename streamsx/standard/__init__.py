# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2017

import enum

__all__ = ['Format', 'Compression']

Format = enum.Enum('Format', 'csv txt bin block line')
Compression = enum.Enum('Compression', 'zlib gzip bzip2')
