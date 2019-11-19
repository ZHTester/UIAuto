import datetime

def message_send(total,pass_n,falied_n,Stotal,Spass_n,Sfalied_n):
    """
    :param Sfalied_n: 体育项目用例失败总数
    :param Spass_n: 体育项目用例通过总数
    :param Stotal: 体育项目用例总数
    :param total: BB项目用例总数
    :param pass_n: BB项目用例通过总数
    :param falied_n: BB项目用例失败总数
    :return:
    """
    mall_send = """
   <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>UI自动化测试报告</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h2 style="font-family: Microsoft YaHei">自动化测试报告</h2>
            <p class='attribute'><strong>测试结果</p>
            <style type="text/css" media="screen">
        body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
        td {text-align:center}
        th {text-align:center}
        </style>
        </head>
        <body>
            <table id='result_table' class="table table-condensed table-bordered table-hover" >
                <colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th width="25%">客户端</th>
                    <th width="25%">用例总数</th>
                    <th width="25%">通过总数</th>
                    <th width="25%">失败总数</th>
                </tr>
                
        <tr class='failClass warning'>
            <td >BB项目UI自动化测试</td>
            <td>"""+str(total)+"""</td>
            <td>"""+str(pass_n)+"""</td>
            <td>"""+str(falied_n)+"""</td>
        </tr>
        
        <tr class='failClass warning'>
            <td >体育项目UI自动化测试</td>
            <td>"""+str(Stotal)+"""</td>
            <td>"""+str(Spass_n)+"""</td>
            <td>"""+str(Sfalied_n)+"""</td>
        </tr>
            </table>
        <!-- 执行模块 -->
        <p class='attribute'><strong>BB项目-测试详情</p>    
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>场景名称</th>
                    <th>用例总数</th>
                    <th>通过数</th>
                    <th>成功率</th>
                    <th>失败数</th>
                    <th>失败率</th>
                </tr>
                 <tr class='failClass warning'>
                    <th width="15%">IOS</th>
                    <th width="15%">100</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                </tr>    
                    <tr class='failClass warning'>
                    <th width="15%">Android</th>
                    <th width="15%">100</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                </tr>  
                    <tr class='failClass warning'>
                    <th width="15%">H5</th>
                    <th width="15%">100</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                </tr>  
                    <tr class='failClass warning'>
                    <th width="15%">Web</th>
                    <th width="15%">100</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                    <th width="15%">8</th>
                </tr>  
        <p class='attribute'><strong>备注:附件为测试用例详情报告与错误截图</p>
        </body>
        </html>
 
    """
    return mall_send