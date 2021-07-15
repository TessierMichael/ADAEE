import * as lineGraphs from './lineGraphs.js'
import * as heatMapsCases from './heatMapsCases.js'
import * as highlightPoints from './highlightPoints.js'

(function (d3) {
    Promise.all([
        d3.csv("static/data/case1-25.csv", d3.autoType),
        d3.csv("static/data/case1-50.csv", d3.autoType),
        d3.csv("static/data/case2-25.csv", d3.autoType),
        d3.csv("static/data/case2-50.csv", d3.autoType),
        d3.csv("static/data/case3-25.csv", d3.autoType),
        d3.csv("static/data/case3-50.csv", d3.autoType),
        // d3.csv("static/data/case4-25.csv", d3.autoType),
        // d3.csv("static/data/case4-50.csv", d3.autoType),
        // d3.csv("static/data/case5-25.csv", d3.autoType),
        // d3.csv("static/data/case5-50.csv", d3.autoType),
        // d3.csv("static/data/case6-25.csv", d3.autoType),
        // d3.csv("static/data/case6-50.csv", d3.autoType),
        // d3.csv("static/data/case7-25.csv", d3.autoType),
        // d3.csv("static/data/case7-50.csv", d3.autoType),
        // d3.csv("static/data/case8-25.csv", d3.autoType),
        // d3.csv("static/data/case8-50.csv", d3.autoType),
        // d3.csv("static/data/case9-25.csv", d3.autoType),
        // d3.csv("static/data/case9-50.csv", d3.autoType),
        // d3.csv("static/data/case10-25.csv", d3.autoType),
        // d3.csv("static/data/case10-50.csv", d3.autoType),
        // d3.csv("static/data/case11-25.csv", d3.autoType),
        // d3.csv("static/data/case11-50.csv", d3.autoType),
        // d3.csv("static/data/case12-25.csv", d3.autoType),
        // d3.csv("static/data/case12-50.csv", d3.autoType),
        // d3.csv("static/data/case13-25.csv", d3.autoType),
        // d3.csv("static/data/case13-50.csv", d3.autoType),
        // d3.csv("static/data/case14-25.csv", d3.autoType),
        // d3.csv("static/data/case14-50.csv", d3.autoType),
        // d3.csv("static/data/case15-25.csv", d3.autoType),
        // d3.csv("static/data/case15-50.csv", d3.autoType),
        // d3.csv("static/data/case16-25.csv", d3.autoType),
        // d3.csv("static/data/case16-50.csv", d3.autoType),
        // d3.csv("static/data/case17-25.csv", d3.autoType),
        // d3.csv("static/data/case17-50.csv", d3.autoType),
        // d3.csv("static/data/case18-25.csv", d3.autoType),
        // d3.csv("static/data/case18-50.csv", d3.autoType),
        // d3.csv("static/data/case19-25.csv", d3.autoType),
        // d3.csv("static/data/case19-50.csv", d3.autoType),
        // d3.csv("static/data/case20-25.csv", d3.autoType),
        // d3.csv("static/data/case20-50.csv", d3.autoType),
    ]).then(function(cases) {

        build()

        function build(){
            lineGraphs.build()
            highlightPoints.build()
            heatMapsCases.build(cases)
        }

    }).catch(function(err) {
        console.log(err)
    })
})(d3)
