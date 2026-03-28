/**
 * @return {Function}
 */
var createHelloWorld = function() {
    const eai = "Hello World";
    return function(...args) {
        return eai;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */