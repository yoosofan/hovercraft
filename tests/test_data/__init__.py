HTML_OUTPUTS = {
    "simple": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body>'
        b'<div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="0" data-y="0" data-z="0"><h1 '
        b'id="simple-presentation">Simple Presentation</h1><p>This '
        b"presentation has two slides, each with a "
        b'header and some text.</p></div><div class="step step-level-1" '
        b'step="1" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="1600" data-y="0" data-z="0"><h1 '
        b'id="second-slide">Second slide</h1><p>There is no positioning or '
        b'anything fancy.</p></div></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/hovercraft-minimal.js"></script></body></html>'
    ),
    "extra_css": (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title></title><link '
        b'rel="stylesheet" href="css/style.css" media="all"></link><link '
        b'rel="stylesheet" href="css/print.css" media="print"></link><link '
        b'rel="stylesheet" href="css/impressConsole.css" '
        b'media="screen,projection"></link><link rel="stylesheet" '
        b'href="extra.css" media="all"></link><script type="text/javascript" '
        b'src="js/dummy.js"></script></head><body '
        b'class="impress-not-supported"><div id="impress"><div class="step '
        b'step-level-1" step="0" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="0" data-y="0" data-z="0">'
        b'<h1 id="simple-presentation">Simple Presentation</h1><p>This '
        b"presentation has two slides, each with a header and some text.</p>"
        b'</div><div class="step step-level-1" step="1" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="1600" '
        b'data-y="0" data-z="0"><h1 id="second-slide">Second '
        b"slide</h1><p>There is no positioning or anything "
        b'fancy.</p></div></div><div id="hovercraft-help" '
        b'class="show"><table><tr><th>Left, Down, Page Down, Space</th><td>'
        b"Next slide</td></tr><tr><th>Right, Up, Page Up</th><td>Previous "
        b"slide</td></tr><tr><th>H</th><td>Toggle this help</td>"
        b'</tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/gotoSlide.js"></script><script type="text/javascript" '
        b'src="js/MathJax/es5/tex-mml-chtml.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script></body></html>'
    ),
    "extra_js": (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title></title><link '
        b'rel="stylesheet" href="css/style.css" media="all"></link><link '
        b'rel="stylesheet" href="css/print.css" media="print"></link><link '
        b'rel="stylesheet" href="css/impressConsole.css" '
        b'media="screen,projection"></link><script type="text/javascript" '
        b'src="js/dummy.js"></script></head><body '
        b'class="impress-not-supported"><div id="impress"><div class="step '
        b'step-level-1" step="0" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="0" data-y="0" data-z="0">'
        b'<h1 id="simple-presentation">Simple Presentation</h1><p>This '
        b"presentation has two slides, each with a header and some text.</p>"
        b'</div><div class="step step-level-1" step="1" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="1600" '
        b'data-y="0" data-z="0"><h1 id="second-slide">Second '
        b"slide</h1><p>There is no positioning or anything "
        b'fancy.</p></div></div><div id="hovercraft-help" '
        b'class="show"><table><tr><th>Left, Down, Page Down, Space</th><td>'
        b"Next slide</td></tr><tr><th>Right, Up, Page Up</th><td>Previous "
        b"slide</td></tr><tr><th>H</th><td>Toggle this help</td>"
        b'</tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/gotoSlide.js"></script><script type="text/javascript" '
        b'src="js/MathJax/es5/tex-mml-chtml.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script><script type="text/javascript" '
        b'src="extra.js"></script></body></html>'
    ),
    "advanced": (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title>Presentation '
        b'title</title><link rel="stylesheet" href="css/style.css" '
        b'media="all"></link><link rel="stylesheet" href="css/print.css" '
        b'media="print"></link><link rel="stylesheet" '
        b'href="css/impressConsole.css" media="screen,projection"></link>'
        b'<link rel="stylesheet" href="extra.css" media="screen"></link>'
        b'<script type="text/javascript" src="js/dummy.js"></script></head>'
        b'<body class="impress-not-supported"><div id="impress" '
        b'data-transition-duration="2000" auto-console="True"><div '
        b'class="step step-level-1" step="0" data-x="1000" data-y="1600" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-z="0"><h1 id="advanced-presentation">Advanced '
        b"Presentation</h1><p>Here we show the positioning feature, where we "
        b"can explicitly set a position\non one of the steps.</p></div><div "
        b'class="step step-level-1" step="1" id="name-this-step" '
        b'data-x="2600" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-y="1600" data-z="0"><h1 id="formatting">'
        b"Formatting</h1><p>Let us also try some basic formatting, like <em>"
        b"italic</em>, and <strong>bold</strong>.</p><ul><li>We can also</li>"
        b'<li>have a list</li><li>of things.</li></ul></div><div class="step '
        b'step-level-1" step="2" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="4200" data-y="1600" '
        b'data-z="0"><p>There should also be possible to have\npreformatted '
        b'text for code.</p><pre class="highlight code python"><span '
        b'class="k">def</span> <span class="nf">foo</span><span class="p">'
        b'(</span><span class="n">bar</span><span class="p">):</span>\n    '
        b'<span class="c1"># Comment</span>\n    <span class="n">a</span> '
        b'<span class="o">=</span> <span class="mi">1</span> <span class="o">'
        b'+</span> <span class="s2">"hubbub"</span>\n    <span class="k">'
        b'return</span> <span class="kc">None</span></pre></div><div '
        b'class="step step-level-1" step="3" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="5800" '
        b'data-y="1600" data-z="0"><p>An image, with attributes:</p><img '
        b'src="images/hovercraft_logo.png" width="50%" '
        b'class="imageclass"></img></div><div class="step step-level-1" '
        b'step="4" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="7400" data-y="1600" data-z="0"><h1 '
        b'id="character-sets">Character sets</h1><p>The character set is '
        b"UTF-8 as of now. Like this: &#xE5;&#xE4;&#xF6;.</p></div></div>"
        b'<div id="hovercraft-help" class="show"><table><tr><th>Left, Down, '
        b"Page Down, Space</th><td>Next slide</td></tr><tr><th>Right, Up, "
        b"Page Up</th><td>Previous slide</td></tr><tr><th>H</th><td>Toggle "
        b'this help</td></tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/gotoSlide.js"></script><script type="text/javascript" '
        b'src="js/MathJax/es5/tex-mml-chtml.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script><script type="text/javascript" '
        b'src="extra.js"></script></body></html>'
    ),
    "default-template": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>'
        b"<title>Presentation title</title>"
        b'<meta charset="UTF-8"></meta><meta name="generator" content='
        b'"Hovercraft! 1.0 http://regebro.github.io/hovercraft"></meta>'
        b'<link rel="stylesheet" href="css/hovercraft.css" media="all"></link>'
        b'<link rel="stylesheet" href="css/highlight.css" media="all"></link>'
        b'<link rel="stylesheet" href="extra.css" media="screen"></link>'
        b"""<script type="text/x-mathjax-config">
      MathJax.Hub.Config({
        showProcessingMessages: false,
        messageStyle: "none",
        TeX : { extensions : ['color.js'] }
      });
    </script>"""
        b'</head><body class="impress-not-supported">'
        b'<div id="impress-help"></div><div id="impress" '
        b'data-transition-duration="2000" auto-console="True"><div '
        b'class="step step-level-1" step="0" data-x="1000" data-y="1600" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-z="0"><h1 id="advanced-presentation">Advanced '
        b"Presentation</h1><p>Here we show the positioning feature, where we "
        b"can explicitly set a position\non one of the steps.</p></div><div "
        b'class="step step-level-1" step="1" id="name-this-step" '
        b'data-x="2600" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-y="1600" data-z="0"><h1 id="formatting">'
        b"Formatting</h1><p>Let us also try some basic formatting, like "
        b"<em>italic</em>, and <strong>bold</strong>.</p><ul><li>"
        b"We can also</li><li>have a list</li><li>of things.</li></ul></div>"
        b'<div class="step step-level-1" step="2" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="4200" '
        b'data-y="1600" data-z="0"><p>There should also be possible to '
        b'have\npreformatted text for code.</p><pre class="highlight code'
        b' python"><span class="k">def</span> <span class="nf">foo</span>'
        b'<span class="p">(</span><span class="n">bar</span>'
        b'<span class="p">):</span>\n    <span class="c1">'
        b'# Comment</span>\n    <span class="n">a</span> <span class="o">='
        b'</span> <span class="mi">1</span> <span class="o">+</span> <span '
        b'class="s2">"hubbub"</span>\n    <span class="k">return</span> <span '
        b'class="kc">None</span></pre></div><div class="step step-level-1" '
        b'step="3" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="5800" data-y="1600" data-z="0"><p>An image,'
        b' with attributes:</p><img src="images/hovercraft_logo.png" '
        b'width="50%" class="imageclass"></img></div><div class="step '
        b'step-level-1" step="4" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="7400" data-y="1600" '
        b'data-z="0"><h1 id="character-sets">Character sets</h1>'
        b"<p>The character set is UTF-8 as of now. Like this: "
        b"&#xE5;&#xE4;&#xF6;.</p></div></div>"
        b'<script type="text/javascript" src="js/impress.js"></script>'
        b'<script type="text/javascript" src="js/gotoSlide.js"></script>'
        b'<script type="text/javascript" src="js/hovercraft.js"></script>'
        b'<script type="text/javascript" src="js/MathJax/es5/tex-mml-chtml.js"></script>'
        b'<script type="text/javascript" src="extra.js"></script>'
        b"</body></html>"
    ),
    "presenter-notes": (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title>Document '
        b'title</title><link rel="stylesheet" href="css/style.css" '
        b'media="all"></link><link rel="stylesheet" href="css/print.css" '
        b'media="print"></link><link rel="stylesheet" '
        b'href="css/impressConsole.css" media="screen,projection"></link>'
        b'<script type="text/javascript" src="js/dummy.js"></script></head>'
        b'<body class="impress-not-supported"><div id="impress"><div '
        b'class="step step-level-1" step="0" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="0" '
        b'data-y="0" data-z="0"><h1 '
        b'id="hovercrafts-presenter-notes">Hovercrafts presenter notes</h1>'
        b"<p>Hovercraft! supports presenter notes. It does this by taking "
        b'anything in a\nwhat is called a "notes-admonition" and making that '
        b'into presenter notes.</p><div class="notes"><p>Hence, this will '
        b"show up as presenter notes.\nYou have still access to a lot of "
        b"formatting, like</p><ul><li>Bullet lists</li><li>And <em>all</em> "
        b"types of <strong>inline formatting</strong></li></ul></div></div>"
        b'<div class="step step-level-1" step="1" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="1600" '
        b'data-y="0" data-z="0"><img '
        b'src="images/hovercraft_logo.png"></img><div class="notes">'
        b"<p>You don't have to start the text on the same line as\nthe note, "
        b"but you can.</p><p>You can also have several paragraphs. You can "
        b"not have any\nheadings of any kind though.</p><p><strong>But you "
        b"can fake them through bold-text</strong></p><p>And that's useful "
        b"enough for presentation notes.</p></div></div></div><div "
        b'id="hovercraft-help" class="show"><table><tr><th>Left, Down, Page '
        b"Down, Space</th><td>Next slide</td></tr><tr><th>Right, Up, Page "
        b"Up</th><td>Previous slide</td></tr><tr><th>H</th><td>Toggle this "
        b'help</td></tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script></body></html>'
    ),
    "skip-presenter-notes": (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title>Document title'
        b'</title><link rel="stylesheet" href="css/style.css" media="all">'
        b'</link><link rel="stylesheet" href="css/print.css" media="print">'
        b'</link><link rel="stylesheet" href="css/impressConsole.css" '
        b'media="screen,projection"></link><script type="text/javascript" '
        b'src="js/dummy.js"></script></head><body '
        b'class="impress-not-supported"><div id="impress"><div class="step '
        b'step-level-1" step="0" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="0" data-y="0" data-z="0">'
        b'<h1 id="hovercrafts-presenter-notes">Hovercrafts presenter notes'
        b"</h1><p>Hovercraft! supports presenter notes. It does this by "
        b'taking anything in a\nwhat is called a "notes-admonition" and '
        b'making that into presenter notes.</p></div><div class="step '
        b'step-level-1" step="1" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="1600" data-y="0" '
        b'data-z="0"><img src="images/hovercraft_logo.png">'
        b'</img></div></div><div id="hovercraft-help" class="show"><table><tr>'
        b"<th>Left, Down, Page Down, Space</th><td>Next slide</td></tr><tr>"
        b"<th>Right, Up, Page Up</th><td>Previous slide</td></tr><tr><th>H"
        b"</th><td>Toggle this help</td></tr></table></div><script "
        b'type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/impressConsole.js"></script><script '
        b'type="text/javascript" src="js/hovercraft.js"></script></body>'
        b"</html>"
    ),
    "table": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
        b'<body><div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="0" data-y="0" data-z="0"><table '
        b'cellpadding="0" cellspacing="0" class="my-table-class">Truth table '
        b'for "not"<thead><tr><th><p>Name</p></th><th><p>Money Owed</p></th>'
        b"</tr></thead><tbody><tr><td><p>Adam Alpha</p></td><td><p>100</p>"
        b'</td></tr></tbody></table><table cellpadding="0" cellspacing="0" '
        b'id="my-table"><thead><tr><th><p>Number</p></th><th><p>Two</p></th>'
        b"</tr></thead><tbody><tr><td><p>Adam Alpha</p></td><td><p>100</p>"
        b"</td></tr></tbody></table></div></div><script "
        b'type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/hovercraft-minimal.js"></script>'
        b"</body></html>"
    ),
    "slide_with_class": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body>'
        b'<div id="impress"><div class="step step-level-1 something-else" '
        b'step="0" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="0" data-y="0" data-z="0"><p>This is some '
        b'text</p></div></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/hovercraft-minimal.js"></script></body></html>'
    ),
    "container_directive": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body>'
        b'<div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="0" data-y="0" data-z="0"><div '
        b'class="my-class"><p>This is some text in the container</p></div>'
        b'<div id="my-thing"><p>This should have an id</p></div></div></div>'
        b'<script type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/hovercraft-minimal.js"></script>'
        b"</body></html>"
    ),
    "class_directive": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body>'
        b'<div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="0" data-y="0" data-z="0"><p class="my-class">'
        b"This is some text in the class</p></div></div><script "
        b'type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/hovercraft-minimal.js"></script>'
        b"</body></html>"
    ),
    "comment": (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body>'
        b'<div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="0" data-y="0" data-z="0"><p>This text '
        b'should appear.</p></div></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/hovercraft-minimal.js"></script></body></html>'
    ),
}
