# AVANTOPS AI - Architecture and product outline

## Product goal

AVANTOPS AI is a premium iPhone app for crypto trading intelligence. It combines:
- signal engine
- portfolio monitoring
- paper trading
- live order confirmation using user-owned API keys
- analytics and premium subscriptions

## Core modules

### Backend
- auth APIs
- portfolio APIs
- signals APIs
- orders APIs
- subscription APIs
- strategy + risk services
- Binance integration

### Mobile
- dashboard overview
- signals list
- portfolio history
- settings and billing
- API key entry

## Security

- Store API keys encrypted at rest
- Use Keychain on iOS
- Require JWT auth
- Validate trade inputs
- Support testnet before real orders

## Recommended monetization

- Free paper trading
- Premium monthly plan
- Annual plan discount
- Low-fee model via exchange fees retained by user
