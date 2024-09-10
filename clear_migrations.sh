#!/bin/bash
migrations=$(locate $(pwd)*/migrations/*0*.py)
for file in $migrations;do rm $file |echo;done
