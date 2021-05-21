from xml.etree.ElementTree import Element, tostring

CHARMAP = {
    'plus or minus': 'plusmn',
    'plus/minus': 'plusmn'
}


def create_element(tag, text=None, attributes=None, children=()):
    """
    A one-liner to create an eTree element
    """
    element = Element(tag, **(attributes if attributes else {}))
    element.text = text or ""

    for child in children:
        element.append(child)

    return element


def mrow(elements):
    """
    Surrounds an element in <mrow> tags, unless it's already surrounded
    """

    m = create_element('mrow')

    if type(elements) != list:
        elements = [elements]

    for element in elements:
        m.append(element)
    
    return m


def number(n):
    return create_element('mn', str(n))


def operator(o):
    return create_element('mo', o)


def symbol(s):
    return create_element('mi', s)


def text(t):
    return create_element('mtext', t)


def superscript(base, sup):
    return mrow(create_element(
        'msup',
        children=[
            mrow(base),
            mrow(sup)
        ]
    ))


def special_char(char):
    return symbol('&' + CHARMAP.get(char, '#65110') + ';')


def subscript(base, sub):
    return create_element('msub', children=(mrow(base), mrow(sub)))


def fraction(numer, denom):
    return create_element('mfrac', children=(mrow(numer), mrow(denom)))


def sqrt(term):
    return create_element('msqrt', children=(mrow(term)))
