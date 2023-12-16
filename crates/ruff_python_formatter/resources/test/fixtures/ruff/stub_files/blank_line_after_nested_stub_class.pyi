class Outer:
    pass
class Outer:
    class OnlyEllipsis: ...
    class OnlyEllipsis: ...
    class OnlyPass:
        pass
    # comment 1
    class Comment1:
        pass
    # comment 2
    class Comment2:
        pass
    # comment 3
    class Comment3: ...
    # comment 4
    class Comment4: ...
    @decorator
    class WithDecorator:
        pass
    @decorator
    class WithDecoratorAndEllipsis: ...
    @decorator
    class WithDecoratorAndEllipsis: ...
    class Nesting1:
        foo: int
        def bar(): pass
    field = 1



    class AfterMultipleEmptyLines:
        pass




