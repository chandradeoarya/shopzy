<h1 align="center">Django & Vue based headless e-commerce platform</h1> <br>

<p align="center">
  A modular, high performance, headless e-commerce platform built with Python, Django, Zappa, and AWS Lambda.
</p>

<p align="center">
 <a href="https://github.com/chandradeoarya/shopzy-storefront" />
  Shopzy-storefront: <br>Github repo of Vuejs based frontend for Shopzy
</p>

<p align="center">
 <a href="https://test.html/" />
  Live demo- coming soon
</p>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Build and Deployment](#build-and-deployment)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

#### Background

An open-source, serverless e-commerce platform delivering ultra-fast, dynamic and personalized shopping experiences.

#### Primary Goal

Shopzy natively decouples the presentation layer from your core business and helps you manage any number of storefronts, apps, and devices from a single back-end. You can create beautiful, engaging brand experiences. Bullet-proof your development workflow and content strategy.

End of the era of a specialized, closed-source knowledge and proprietary templates. Just Django, Vue and with power and flexibility of serverless using AWS Lambda. We are working hard to reduceWe obsess over the right abstractions so your teams don’t need to stitch together disparate systems, or spend months integrating payments functionality. Create beautiful experiences and powerful extensions through Webhooks/PubSub and the GraphQL API.

## Features

A few of the things you can do with Shopzy:

- Handle all requests by axios and interceptor
- JWT based authentication
- Redirect when token expired or not logged in
- Handle JWT with Vuex to store states
- Save states into local storage
- Integrate backend API
- API support login, create, update, delete risk
- API support CRUD functionality create, update, delete Fields
- API support types text, date, enum, number to a specific risk.
- Test cases
- Local development and test setup
- Zappa django serverless deployment steps
- Vue build and decoupled AWS S3 static hosting
- Headless commerce: Build mobile apps, customize storefronts and externalize processes
- UX and UI: Designed for a user experience that rivals even the top commercial platforms
- Dashboard: Administrators have total control of users, processes, and products
- Orders: A comprehensive system for orders, dispatch, and refunds
- Cart: Advanced payment and tax options, with full control over discounts and promotions
- Payments: Flexible API architecture allows integration of any payment method. It comes with Braintree support out of the box.
- Cloud: Optimized for deployments on AWS using AWS Lambda, S3, API-gateway

<p align="center">
  <img src = "https://github.com/chandradeoarya/shopzy-storefront/blob/master/screenshots/home.png?raw=true" width=700>
</p>

<p align="center">
  <img src = "https://github.com/chandradeoarya/shopzy-storefront/blob/master/screenshots/product.png?raw=true" width=700>
</p>

<p align="center">
  <img src = "https://github.com/chandradeoarya/shopzy-storefront/blob/master/screenshots/cart.png?raw=true" width=700>
</p>

<p align="center">
  <img src = "https://github.com/chandradeoarya/shopzy-storefront/blob/master/screenshots/payment.png?raw=true" width=700>
</p>

## Setup

### Backend setup for local development

```

$ python3 -m venv venv

''' activate virtual env '''
$ source venv/bin/activate

'''install dependencies'''
$ pip3 install -r requirements.txt

'''create migrations'''
$ python manage.py makemigrations profiles risks

'''migrate'''
$ python manage.py migrate

'''create super user'''
$ python manage.py createsuperuser

'''run development server on http://127.0.0.1:8000'''
$ python manage.py runserver

'''unit tests'''
$ python manage.py test
```

#### setup frontend for local development

```
cd frontend

''' install dependencies '''
npm install

''' serve with hot reload at http://127.0.0.1:8080 '''
npm start
```

## Build-and-Deployment

The project has been built and deployed at [Shopzy demo with storefront](https://shopzy-storefront.vercel.app/).

#### Making Backend ready for deployment

1.  Set DEBUG= False in setting.py
2.  Add public address and ip in allowed hosts
3.  Please give a unique django secret key. eg. [django-secret-key-generator](https://miniwebtool.com/django-secret-key-generator/)
4.  Add AWS S3 bucket url in CORS_ORIGIN_WHITELIST.
