export function build () {
    console.log('building metric')
    
    d3.select('#adaptive_metric_container svg')
    .attr('width', '100%')
    .attr('height', '100%')
    
    let g = d3.select('#adaptive_metric_container svg')

    let metric = g.select('text').node() ? g.select('text') : g.append('text')

    let metricValue = 88

    let maxWidth = g.node().getBoundingClientRect().width
    let maxHeight = g.node().getBoundingClientRect().height

    metric.text(`${metricValue}`)
    .attr('x', maxWidth/2)
    .attr('y', maxHeight/2)
    .attr('text-anchor', 'middle')
    .attr('font-size', '60px')
}