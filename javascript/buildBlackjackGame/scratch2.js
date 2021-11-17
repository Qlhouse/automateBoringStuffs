const bar = () => {
    throw new DOMException()
}

const baz = () => console.log('baz')

const foo = () => {
    console.log('foo')
    setTimeout(bar, 2)
    bar()
    baz()
}

foo()