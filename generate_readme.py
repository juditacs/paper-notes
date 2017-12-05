#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Judit Acs <judit@sch.bme.hu>
#
# Distributed under terms of the MIT license.

import os
import re


def parse_papers(text):
    title_re = re.compile("^## ", re.MULTILINE)
    author_re = re.compile("^### ([^\d,]*),?\s*([0-9]{4})", re.MULTILINE)
    for part in title_re.split(text):
        paper = {}
        paper['title'] = part.split("\n")[0].strip()
        if not paper['title']:
            continue
        m = author_re.search(part)
        paper['authors'] = m.group(1).strip()
        paper['year'] = m.group(2).strip()
        yield paper


def main():
    topics = {}
    cwd = os.path.dirname(os.path.realpath(__file__))
    for fn in os.listdir(cwd):
        if not fn.endswith(".md") or fn.lower() == "readme.md":
            continue
        with open(os.path.join(cwd, fn)) as f:
            title = next(f)
            assert title.startswith("# ")
            title = title.lstrip("# ").strip()
            topics[title] = []
            for paper in parse_papers(f.read()):
                paper['url'] = "{}#{}".format(fn, paper['title'].lower().replace(" ", "-"))
                topics[title].append(paper)
    with open(os.path.join(cwd, "README.md"), "w") as f:
        f.write("# Papers I read\n\n")
        for topic, papers in sorted(topics.items()):
            f.write("## {}\n\n".format(topic))
            for paper in sorted(papers, key=lambda x: x['authors']):
                f.write("[{0}, {1}. {2}]({3})\n\n".format(paper['authors'], paper['year'], paper['title'], paper['url']))



if __name__ == '__main__':
    main()
