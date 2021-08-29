# DevOps

![build](https://github.com/matveyplevako/devops/actions/workflows/deploy.yml/badge.svg)

## Description

This app displays current time in Moscow

## App

App that returns Moscow time is located at app_python/
\
Docker image is located at [dockerhub](https://hub.docker.com/repository/docker/matveyplevako/lab2)

## How to run?

`uvicorn app_python.main:app`

## Action stages

1. **lint** runs flake8 checks
2. **test** runs pytest
3. **deploy** if lint and test succeed, image is build and deployed to dockerhub

## Unit tests

To run tests run `pytest`

## Linter

to run lint run `flake8 app_python` 
