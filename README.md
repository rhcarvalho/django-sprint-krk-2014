Killing typos during Django Sprint 2014 in Kraków
=================================================

This repo contains some quick-and-dirty scripts I used to find and fix typos in the [Django](https://www.djangoproject.com) [Documentation](https://docs.djangoproject.com) on the weekend of the 15th and 16th of February, 2014.

It all started when pairing with [Tyler Golden](https://twitter.com/tylersiprova). We decided to fix some misspelling-related tickets.
She had very clever heuristics to find common British x American spelling mistakes.

I took it further and automated things. Still, it was a big pain to go through the potential typos one by one...

The resulting work was a bunch of Pull Requests: [#2281](https://github.com/django/django/pull/2281), [#2282](https://github.com/django/django/pull/2282), [#2283](https://github.com/django/django/pull/2283), [#2285](https://github.com/django/django/pull/2285), [#2288](https://github.com/django/django/pull/2288), [#2284](https://github.com/django/django/pull/2284), [#2285](https://github.com/django/django/pull/2285), [#2286](https://github.com/django/django/pull/2286).

I don't know/remember why I've split the changes into so many PRs.

During the very same Sprint, [Piotr Kasprzyk](https://github.com/kwadrat) also worked on fixing typos and we've merged our efforts into the latests PRs.

A year later I started working on a follow-up project to spellcheck documentation, [typokiller](https://github.com/rhcarvalho/typokiller).
