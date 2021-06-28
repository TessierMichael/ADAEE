import * as heatMaps from './heatMapsDimensions.js'
import * as lineGraphs from './lineGraphsDimensions.js'
import * as metric from './adaptiveMetric.js'

function build(){
    heatMaps.build()
    lineGraphs.build(null)
    metric.build()
}

//var data = document.querySelector('#mydata')
//var cases = eval('(' + data.dataset.cases + ')')
//console.log(cases)
build()

window.addEventListener('resize', () => {
    build()
})