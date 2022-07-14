def generate_dashboard(cluster_name,endpoint,directory,
    is_single_entity,delete_endpoint,put_endpoint,pks):
    table_headers_orig = list(endpoint['response'].keys())
    table_headers = [header.replace('.',' ').replace('_',' ')  for header in table_headers_orig]
    table_headers_orig = [header.replace('.','_').replace('_','_')  for header in table_headers_orig]
    # cluster_name = endpoint['cluster_name']
    endpoint_name = endpoint['endpoint_name']
    query_params = [(param,d,o,a) for param,d,o,a in endpoint['queryParams']]
    dashboard_string = '''<template>
    <div class="dashboard">
        <div class="sidebar">'''

    if len(query_params)>0:
        dashboard_string += '\t\t<p>Filters</p>\n'
    dashboard_string += '\t\t<form @submit.prevent="call_request">\n'
    dashboard_string += '\t\t<div class="filters">\n'
    for param,datatype,operator,aggregate in query_params:
        param = param.replace('.','_')
        if operator == '<':operator = 'less than'
        elif operator == '>':operator = 'greater than'
        elif operator == '=' or operator == 'is':operator = 'equal to'
        elif operator == '!=':operator = 'not equal to'
        elif operator == '<=':operator = 'less than or equal to'
        elif operator == '>=':operator = 'greater than or equal to'
        elif operator == 'like':operator = 'regex matching (case invariant)'
        elif operator == 'not like':operator = 'regex matching (case invariant)'
        if not operator: operator = 'equal to'

        
        if datatype == 'str':datatype = 'text'
        elif datatype == 'int' or datatype == 'float':datatype = 'number'
        elif datatype=='bool':datatype = 'checkbox'
        elif datatype == 'date':datatype = 'date'
        else: datatype = 'text'
        dashboard_string += '\t\t<div class="input_section">\n'
        dashboard_string += '\t\t<div class="labels">\n'
        dashboard_string += '\t\t<label>'+ param +'</label>\n'
        if aggregate: dashboard_string += '\t\t<label> aggregate '+ aggregate+'</label><br>\n'
        dashboard_string += '\t\t<label> operation '+ operator +'</label>\n'
        dashboard_string += '\t\t</div>\n'
        dashboard_string += '\t\t<div>\n'

        if operator == 'between':
            dashboard_string += f'\t\t<input placeholder="from" type="{datatype}" v-model="{param}[0]" class="{datatype}" required>\n'
            dashboard_string += f'\t\t<input placeholder="to" type="{datatype}" v-model="{param}[1]" class="{datatype}" required>\n'
        else:
            if datatype=='checkbox':
                dashboard_string += f'\t\t<input type="{datatype}" v-model="{param}" class="{datatype}">\n' 
                dashboard_string += '\t\t<label>Set Value</label>\n'
            else:
                dashboard_string += f'\t\t<input type="{datatype}" v-model="{param}" class="{datatype}" required>\n'
        
        dashboard_string += '\t\t</div>\n'
        dashboard_string += '\t\t</div>\n'

    dashboard_string += '\t\t</div>\n'  
    dashboard_string +='''
        <input type="submit"
        value="Call endpoint"
        class="button"
        >
        </form>
        </div>
<div class="content">
        <div class="table_nav">
        '''
    dashboard_string += '<h2>'+cluster_name+'</h2>'
    dashboard_string +=    '''
    </div>
    '''
    dashboard_string += '<h3>'+endpoint_name+'</h3>'
    dashboard_string += '''
    <div>
        <table class="dashboard_table">
        <tr v-if='dashboard_data.length>0'>\n'''
    for header in table_headers:
        dashboard_string += '\t\t<th>' + header + '</th>\n'
    dashboard_string += '\t\t</tr>'
    dashboard_string +=  "<tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>\n"
    for header in table_headers_orig:
        dashboard_string += '\t\t\t<td>{{row.' + header + '}}</td>\n'
    if is_single_entity:
        dashboard_string += '''
                <td class="editIcon" @click="route_edit(row)">
                    <i class="fa fa-edit"></i>
                </td>
                <td class="trashIcon"  @click="delete_obj(row)">
                    <i class="fa fa-trash" aria-hidden="true"></i>
                </td>
        '''
    dashboard_string += '\t\t</tr>'
    dashboard_string += '''
        </table>
        </div>
        </div>
    </div>
</template>
<style lang="scss" scoped>
@import "../scss/dashboard.scss";
</style>
<script>
    import { mapState } from "vuex";
    export default {
    name: "dashBoard",
    props: {},
    data: function () {
    return {
'''
    for param,_,op,_ in query_params:
        if op == 'between':
            dashboard_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + '[0,100],\n'
        else:
            dashboard_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + '"",\n'
    
    dashboard_string += '''
    };
    },
    computed: {
    ...mapState({
    '''
    dashboard_string += 'dashboard_data: state => state.'\
                    +cluster_name+'.'+endpoint_name+',\n'
    dashboard_string += '''}),},
    methods: {
    call_request() {
    '''
    dashboard_string+= 'this.$store.dispatch("'+cluster_name +'/'+endpoint_name +'",\n\t\t {'
    for param,_,_,_ in query_params:
        dashboard_string += "'"+param+"'" +': this.' + param.replace('.','_').replace(' ','_') + ',\n\t\t'
    dashboard_string += '''
      });
    },
    async delete_obj(obj) {
    '''
    dashboard_string+= 'await this.$store.dispatch("'+cluster_name +'/'+delete_endpoint +'",\n\t\t {'
    for pk,_ in pks:
        dashboard_string += pk +': obj.' + pk + ',\n\t\t'
    dashboard_string += '''
      });
      this.call_request();
    },
    route_edit(obj) {
    '''
    dashboard_string+= 'let route = "'+cluster_name +'_'+put_endpoint +'/"'
    for pk,_ in pks:
        dashboard_string += '+obj.' + pk + '+"_"'

    dashboard_string += ''';
    this.$router.push({
      path: route,
    });
    }
    }
    };
</script>
    '''
    f = open(directory, "w")
    f.write(dashboard_string)
    f.close()