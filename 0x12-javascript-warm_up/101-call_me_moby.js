#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (typeof theFunction === 'function') {
    // theFunction is a function, so it's safe to call it
    for (let i = x; i > 0; i--) {
      theFunction();
    }
  }
};
