
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta, timezone
import random

def plot_similarity(data, triangle_legend, circle_legend):
    dates = []
    similarities = []
    reason_segments = []
    messages = []
    offsets_x = []
    offsets_y = []

    # 解析数据
    for item in data:
        date = datetime.strptime(item['date'], '%a %b %d %H:%M:%S %Y %z')
        dates.append(date)
        similarities.append(item['similarity'])
        reason_segments.append(item['reasonSegment'])
        messages.append(item['message'])
        offsets_x.append(item.get('offset_x', 0))
        offsets_y.append(item.get('offset_y', 0))

    # 确保所有日期对象都是 offset-aware
    def make_offset_aware(dt):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt

    dates = [make_offset_aware(date) for date in dates]
    start_date = make_offset_aware(dates[0])
    end_date = make_offset_aware(dates[-1])

    # 创建图形，并缩短高度
    fig, ax = plt.subplots(figsize=(10, 4))  # 调整figsize来缩短高度
    ax.set_ylim(0, 1)

    # 绘制折线
    ax.plot(dates, similarities, label='Similarity')

    # 获取每一年的第一天
    year_dates = [make_offset_aware(datetime(year, 1, 1, tzinfo=timezone.utc)) for year in range(start_date.year, end_date.year + 1)]
    vlines_dates = year_dates

    # 去重并排序
    vlines_dates = sorted(set(vlines_dates))

    # 绘制点
    for i in range(len(dates)):
        if reason_segments[i] == 0:
            ax.scatter(dates[i], similarities[i], marker='^', color='blue', s=50)
        elif reason_segments[i] == 1:
            ax.scatter(dates[i], similarities[i], marker='o', color='red', s=50)
        if messages[i]:
            date_str = dates[i].strftime('%Y-%m-%d')
            message_with_date = f"{messages[i]}\n{date_str}"
            ax.annotate(
                message_with_date,
                xy=(dates[i], similarities[i]),
                xytext=(dates[i] + timedelta(days=offsets_x[i]), similarities[i] + offsets_y[i]),
                textcoords='data',
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='black'),
                fontsize=25  # 设置更大的字体大小
            )

    # 绘制纵向辅助线
    for line_date in vlines_dates:
        ax.axvline(x=line_date, color='gray', linestyle='--', linewidth=1)

    # 设置横坐标标签
    ax.set_xticks(year_dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # 水平显示横轴标签，并增大字体
    plt.xticks(rotation=0, ha='center', fontsize=30)

    # 墛大纵坐标标签字体
    ax.tick_params(axis='y', labelsize=25)

    # 添加图例
    triangle_proxy = plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='blue', markersize=20)
    circle_proxy = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=20)
    ax.legend([triangle_proxy, circle_proxy], [triangle_legend, circle_legend], fontsize=30)

    # 移动并增大横坐标标题
    ax.set_xlabel('Date', fontsize=30, labelpad=20, loc='right')
    # plt.xlabel('Date', fontsize=30, labelpad=20, loc='right')
    ax.xaxis.set_label_coords(1.02, 0)

    
    # 移动并增大纵坐标标题
    ax.set_ylabel('Similarity', fontsize=30, labelpad=30)
    # ax.yaxis.set_label_position('left')
    ax.yaxis.set_label_coords(0, 1.02)
    ax.yaxis.label.set_rotation(0)

    
    plt.grid(True)
    plt.show()


# C    
# data =[
# {'date': 'Tue Oct 18 23:24:51 2016 +0300', 'dataStamp': 1476822291.0, 'similarity': 0.32242990654205606, 'reasonSegment': 1, 'message': '1: Defect added.',"offset_x": 200, "offset_y": 0.13}, 
# {'date': 'Thu Nov 10 10:45:10 2016 +0100', 'dataStamp': 1478771110.0, 'similarity': 0.3177570093457944, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Nov 16 16:24:27 2016 +0100', 'dataStamp': 1479309867.0, 'similarity': 0.3317757009345794, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Dec 14 08:33:50 2016 +0200', 'dataStamp': 1481697230.0, 'similarity': 0.32242990654205606, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Dec 20 19:58:03 2016 +0200', 'dataStamp': 1482256683.0, 'similarity': 0.32866043613707163, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Dec 21 17:49:39 2016 +0200', 'dataStamp': 1482335379.0, 'similarity': 0.35358255451713394, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Dec 22 13:45:41 2016 +0200', 'dataStamp': 1482407141.0, 'similarity': 0.3302180685358255, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Sun Dec 25 11:20:32 2016 +0200', 'dataStamp': 1482657632.0, 'similarity': 0.3411214953271028, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon Jan 2 13:43:12 2017 +0200', 'dataStamp': 1483357392.0, 'similarity': 0.35358255451713394, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Jan 11 16:15:01 2017 +0200', 'dataStamp': 1484144101.0, 'similarity': 0.34890965732087226, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Jan 17 11:01:47 2017 +0200', 'dataStamp': 1484643707.0, 'similarity': 0.35358255451713394, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Jan 18 17:01:01 2017 -0800', 'dataStamp': 1484787661.0, 'similarity': 0.35358255451713394, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Fri Jan 27 14:35:00 2017 -0600', 'dataStamp': 1485549300.0, 'similarity': 0.35202492211838005, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Feb 1 17:37:14 2017 +0200', 'dataStamp': 1485963434.0, 'similarity': 0.37538940809968846, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Mar 14 15:00:15 2017 +0200', 'dataStamp': 1489496415.0, 'similarity': 0.38161993769470404, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Apr 20 11:27:56 2017 +0300', 'dataStamp': 1492676876.0, 'similarity': 0.3894080996884735, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Apr 20 12:00:29 2017 -0500', 'dataStamp': 1492707629.0, 'similarity': 0.3909657320872274, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu May 4 11:25:28 2017 +0300', 'dataStamp': 1493886328.0, 'similarity': 0.3956386292834891, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon May 8 18:03:02 2017 +0200', 'dataStamp': 1494259382.0, 'similarity': 0.3598130841121495, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed May 10 16:27:16 2017 +0200', 'dataStamp': 1494426436.0, 'similarity': 0.3613707165109034, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Aug 9 09:21:11 2017 +0300', 'dataStamp': 1502259671.0, 'similarity': 0.367601246105919, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Jul 17 10:35:52 2018 +0300', 'dataStamp': 1531812952.0, 'similarity': 0.37227414330218067, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon Jun 17 15:54:45 2019 +0300', 'dataStamp': 1560776085.0, 'similarity': 0.3987538940809969, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Jun 25 12:25:32 2019 -0400', 'dataStamp': 1561479932.0, 'similarity': 0.37227414330218067, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Fri Jun 28 12:09:36 2019 +0300', 'dataStamp': 1561712976.0, 'similarity': 0.40186915887850466, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Nov 12 13:41:30 2019 +0200', 'dataStamp': 1573558890.0, 'similarity': 0.37850467289719625, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Nov 12 17:02:13 2019 +0200', 'dataStamp': 1573570933.0, 'similarity': 0.38006230529595014, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Nov 26 20:54:58 2019 +0200', 'dataStamp': 1574794498.0, 'similarity': 0.38161993769470404, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Jan 16 17:21:12 2020 +0100', 'dataStamp': 1579191672.0, 'similarity': 0.38161993769470404, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Mar 18 17:09:20 2020 -0700', 'dataStamp': 1584576560.0, 'similarity': 0.618380062305296, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Mar 19 12:31:20 2020 -0700', 'dataStamp': 1584646280.0, 'similarity': 0.8598130841121495, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon Apr 6 13:33:41 2020 +0200', 'dataStamp': 1586172821.0, 'similarity': 0.9548286604361371, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Apr 7 14:32:43 2020 -0700', 'dataStamp': 1586295163.0, 'similarity': 0.9392523364485982, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Apr 23 13:08:20 2020 -0700', 'dataStamp': 1587672500.0, 'similarity': 0.9485981308411215, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Fri May 1 23:11:52 2020 -0700', 'dataStamp': 1588399912.0, 'similarity': 0.956386292834891, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon May 4 10:02:26 2020 -0700', 'dataStamp': 1588611746.0, 'similarity': 0.9829192546583851, 'reasonSegment': 1, 'message': '2: Clone target.',"offset_x": -200, "offset_y": 0.08}, 
# {'date': 'Tue May 12 13:53:54 2020 -0700', 'dataStamp': 1589316834.0, 'similarity': 0.8757062146892656, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed May 27 11:26:57 2020 -0500', 'dataStamp': 1590596817.0, 'similarity': 0.9627329192546584, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Jun 3 14:48:04 2020 +0200', 'dataStamp': 1591188484.0, 'similarity': 0.9309309309309309, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Fri Aug 21 13:45:52 2020 -0700', 'dataStamp': 1598042752.0, 'similarity': 0.9295352323838081, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Fri Jan 8 11:27:54 2021 +0100', 'dataStamp': 1610101674.0, 'similarity': 0.8659217877094972, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Feb 9 08:34:33 2021 +0200', 'dataStamp': 1612852473.0, 'similarity': 0.8744710860366713, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Tue Apr 27 10:38:23 2021 +0200', 'dataStamp': 1619512703.0, 'similarity': 0.8473177441540578, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Oct 14 15:55:16 2021 +0800', 'dataStamp': 1634198116.0, 'similarity': 0.8461538461538461, 'reasonSegment': 0, 'message': '3: Clone generated and defect propagated.',"offset_x": -200, "offset_y": 0.13}, 
# {'date': 'Wed Nov 3 21:09:04 2021 +0530', 'dataStamp': 1635953944.0, 'similarity': 0.8415300546448088, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Sun Nov 21 12:23:19 2021 +1000', 'dataStamp': 1637461399.0, 'similarity': 0.8369565217391305, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Dec 8 15:36:57 2021 +0100', 'dataStamp': 1638974217.0, 'similarity': 0.8426812585499316, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon Jan 24 15:44:29 2022 +0100', 'dataStamp': 1643035469.0, 'similarity': 0.8335588633288228, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Thu Feb 3 16:24:15 2022 +0100', 'dataStamp': 1643901855.0, 'similarity': 0.8268456375838926, 'reasonSegment': 1, 'message': '4: Defect fixed.',"offset_x": -200, "offset_y": -0.23}, 
# {'date': 'Fri May 6 11:12:04 2022 +0200', 'dataStamp': 1651828324.0, 'similarity': 0.8191489361702128, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Mon May 30 16:08:11 2022 +0200', 'dataStamp': 1653919691.0, 'similarity': 0.820855614973262, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Nov 2 14:31:13 2022 +0100', 'dataStamp': 1667395873.0, 'similarity': 0.7925531914893617, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Fri Apr 28 11:09:46 2023 +0200', 'dataStamp': 1682672986.0, 'similarity': 0.7894039735099337, 'reasonSegment': 1, 'message': ''}, 
# {'date': 'Wed Dec 6 14:53:42 2023 +0800', 'dataStamp': 1701845622.0, 'similarity': 0.781127129750983, 'reasonSegment': 1, 'message': ''}
# ]


# x 300 y 0.13
# JS
data = [{'date': 'Mon Apr 11 10:17:45 2016 +0200', 'dataStamp': 1460362665.0, 'similarity': 0.9257950530035336, 'reasonSegment': 1, 'message': '', 'commitId': '41044979d266577a83006fd1b302a916e0ba1628'},
 {'date': 'Fri Jun 24 10:34:41 2016 +0200', 'dataStamp': 1466757281.0, 'similarity': 0.9257950530035336, 'reasonSegment': 0, 'message': '1: Clone generated.', 'commitId': '306874ee3270dd17c01bd9044524249832288eea',"offset_x": -60, "offset_y": 0.13},
 {'date': 'Thu Sep 22 17:59:00 2016 +0200', 'dataStamp': 1474559940.0, 'similarity': 0.8456591639871383, 'reasonSegment': 1, 'message': '', 'commitId': 'f5f2a183174e6dee93d3436982ff48a7baf0329f'},
 {'date': 'Mon Nov 21 12:37:54 2016 +0100', 'dataStamp': 1479728274.0, 'similarity': 0.6276849642004774, 'reasonSegment': 1, 'message': '', 'commitId': 'e0bdc95d318ade5db3613e9d3a068856c0cba22e'},
 {'date': 'Mon Jan 30 16:12:57 2017 +0100', 'dataStamp': 1485789177.0, 'similarity': 0.2791932059447983, 'reasonSegment': 1, 'message': '', 'commitId': '4909f6c5238a569d8f7e91d75d5c942bacb03df5'},
 {'date': 'Fri Mar 10 16:19:47 2017 +0100', 'dataStamp': 1489159187.0, 'similarity': 0.7956131605184447, 'reasonSegment': 0, 'message': '', 'commitId': 'fe95d324abe649a3f78de58cbbe41259c7b961df'},
 {'date': 'Mon Oct 30 16:16:10 2017 +0100', 'dataStamp': 1509376570.0, 'similarity': 0.7866273352999017, 'reasonSegment': 0, 'message': '2: Defect added.', 'commitId': '292d293860f9f23dd860cfb60b0111605df0f7f6',"offset_x": -430, "offset_y": 0.12},
 {'date': 'Thu Dec 21 11:15:56 2017 +0100', 'dataStamp': 1513851356.0, 'similarity': 0.7876106194690266, 'reasonSegment': 1, 'message': '', 'commitId': '4388409c0219569f9bb7df7a9ac7af35717be9d9'},
 {'date': 'Thu Dec 21 16:08:10 2017 +0100', 'dataStamp': 1513868890.0, 'similarity': 0.7925270403146509, 'reasonSegment': 1, 'message': '3: Defect propagated.', 'commitId': 'b9b07298f5ceca4ed836f144717c18dab4b9b88d',"offset_x": -150, "offset_y": -0.3},
 {'date': 'Wed Jan 10 10:08:32 2018 +0100', 'dataStamp': 1515575312.0, 'similarity': 0.796812749003984, 'reasonSegment': 0, 'message': '', 'commitId': '6bb47271b9522b5be77b4559b3f6fb3b95897214'},
 {'date': 'Tue Jan 16 16:43:14 2018 +0100', 'dataStamp': 1516117394.0, 'similarity': 0.7917485265225933, 'reasonSegment': 0, 'message': '', 'commitId': 'f8254142b56a3a5e7d47478b16b8c2b27f38c294'},
 {'date': 'Wed Jan 17 09:52:28 2018 +0100', 'dataStamp': 1516179148.0, 'similarity': 0.7917485265225933, 'reasonSegment': 0, 'message': '4: Defect fixed', 'commitId': 'a63c9fc0237707b41c6082980e9288206d4ad7f0',"offset_x": -200, "offset_y": 0.07},
 {'date': 'Wed Jan 17 16:53:50 2018 +0100', 'dataStamp': 1516204430.0, 'similarity': 0.7899901864573111, 'reasonSegment': 0, 'message': '', 'commitId': 'ae72f520f66e348c280580e8baca8306f93ffd76'},
 {'date': 'Wed Jan 17 20:56:07 2018 +0100', 'dataStamp': 1516218967.0, 'similarity': 0.7909715407262021, 'reasonSegment': 1, 'message': '', 'commitId': '87e0a5336be3874a2ac94515cec8b40bb50a9c78'},
 {'date': 'Wed Jan 17 21:14:06 2018 +0100', 'dataStamp': 1516220046.0, 'similarity': 0.7909715407262021, 'reasonSegment': 1, 'message': '5: Fix propagated', 'commitId': 'ebd0c4099ebcea5af7e69428b1d1e71294342834',"offset_x": 450, "offset_y": 0.08},
 {'date': 'Thu Jan 18 09:27:38 2018 +0100', 'dataStamp': 1516264058.0, 'similarity': 0.7968596663395485, 'reasonSegment': 1, 'message': '', 'commitId': '6303248ebc99a4056ee6788de011c8f8e5a65b9d'},
 {'date': 'Thu Jan 18 09:42:06 2018 +0100', 'dataStamp': 1516264926.0, 'similarity': 0.7988223748773308, 'reasonSegment': 1, 'message': '', 'commitId': '492f3863a6aa3546cd9b3864c7af0d7ed16d0511'},
 {'date': 'Mon Feb 19 16:02:58 2018 +0100', 'dataStamp': 1519052578.0, 'similarity': 0.759927797833935, 'reasonSegment': 1, 'message': '', 'commitId': '760f3c8a00bcfe28ed6df96698abe88a3ff9bd3c'},
 {'date': 'Mon Feb 26 11:14:26 2018 +0100', 'dataStamp': 1519640066.0, 'similarity': 0.759927797833935, 'reasonSegment': 1, 'message': '', 'commitId': '93cfad414288b9f918557d239905100dd5d6976c'},
 {'date': 'Tue Apr 17 12:49:34 2018 +0200', 'dataStamp': 1523962174.0, 'similarity': 0.7988223748773308, 'reasonSegment': 1, 'message': '', 'commitId': 'c41c300fac0a7b4482671dcd4eac1205301ec7b6'},
 {'date': 'Mon Aug 27 09:50:35 2018 +0200', 'dataStamp': 1535356235.0, 'similarity': 0.7798334875115633, 'reasonSegment': 1, 'message': '', 'commitId': 'e4e985a0516e8503f403452d8bda278304ce8878'},
 {'date': 'Mon Aug 27 10:01:20 2018 +0200', 'dataStamp': 1535356880.0, 'similarity': 0.820017559262511, 'reasonSegment': 0, 'message': '', 'commitId': 'dd66d2e41233dbb66419095ac499ea0017acce24'},
 {'date': 'Tue Aug 28 10:05:47 2018 +0200', 'dataStamp': 1535443547.0, 'similarity': 0.8194690265486726, 'reasonSegment': 0, 'message': '', 'commitId': 'a331183e53d3b3e382f95a18f1aa14dfdfb2c3ac'},
 {'date': 'Tue Aug 28 10:07:31 2018 +0200', 'dataStamp': 1535443651.0, 'similarity': 0.8212389380530973, 'reasonSegment': 1, 'message': '', 'commitId': 'e888c7d0d6b26404073b7c6c07a2a25a0eb132c3'},
 {'date': 'Tue Aug 28 13:18:32 2018 +0200', 'dataStamp': 1535455112.0, 'similarity': 0.8221238938053097, 'reasonSegment': 1, 'message': '', 'commitId': 'b3e6334e68ba23d38a9ebf1e7f21a7627045e025'},
 {'date': 'Mon Jan 28 09:26:42 2019 +0100', 'dataStamp': 1548664002.0, 'similarity': 0.8221238938053097, 'reasonSegment': 0, 'message': '', 'commitId': '289d721f1262b699c7cb6ceb73e56af361d9ca82'},
 {'date': 'Mon Jan 28 11:02:17 2019 +0100', 'dataStamp': 1548669737.0, 'similarity': 0.8221238938053097, 'reasonSegment': 1, 'message': '', 'commitId': 'fc391d329fa964c23fb27f634edf3fdbf4538fce'},
 {'date': 'Mon Jan 28 13:16:08 2019 +0100', 'dataStamp': 1548677768.0, 'similarity': 0.8221238938053097, 'reasonSegment': 1, 'message': '', 'commitId': '800e30a20fd934e246d86c7d8c511029aa0e93f4'},
 {'date': 'Mon Jan 28 13:21:37 2019 +0100', 'dataStamp': 1548678097.0, 'similarity': 0.8249128919860628, 'reasonSegment': 0, 'message': '', 'commitId': '4099678e70153f36578a93c806c35c1ebedcd215'},
 {'date': 'Wed Jan 30 13:32:15 2019 +0100', 'dataStamp': 1548851535.0, 'similarity': 0.8249128919860628, 'reasonSegment': 0, 'message': '', 'commitId': '7e183c75ec46616e2cc393a433caa97ef13fa7d1'},
 {'date': 'Wed Jan 30 13:32:30 2019 +0100', 'dataStamp': 1548851550.0, 'similarity': 0.8249128919860628, 'reasonSegment': 1, 'message': '', 'commitId': '300d45738845205c1a1d70153af48b74506c674c'},
 {'date': 'Thu Jan 31 10:12:55 2019 +0100', 'dataStamp': 1548925975.0, 'similarity': 0.8249128919860628, 'reasonSegment': 0, 'message': '', 'commitId': '9a8fe5befdd12b759b55855b80b391c6b2cd1858'},
 {'date': 'Thu Jan 31 10:13:25 2019 +0100', 'dataStamp': 1548926005.0, 'similarity': 0.8249128919860628, 'reasonSegment': 1, 'message': '', 'commitId': '24665603361e1897d336745c9c74d4155b25d565'},
 {'date': 'Fri Feb 1 15:31:49 2019 +0100', 'dataStamp': 1549031509.0, 'similarity': 0.8249128919860628, 'reasonSegment': 0, 'message': '', 'commitId': '5c57098ff1065924d7186ecac4ca9f49fdf07f3f'},
 {'date': 'Fri Feb 1 15:32:24 2019 +0100', 'dataStamp': 1549031544.0, 'similarity': 0.8249128919860628, 'reasonSegment': 1, 'message': '', 'commitId': 'ba09c45936a2d3b99ee7bced816e4ea6ac3181df'},
 {'date': 'Sat Feb 23 01:09:42 2019 +0100', 'dataStamp': 1550880582.0, 'similarity': 0.8249128919860628, 'reasonSegment': 0, 'message': '', 'commitId': 'f90c273e50e0404613bfc0698a2d840172cc13d2'},
 {'date': 'Tue Mar 5 18:46:30 2019 +0100', 'dataStamp': 1551807990.0, 'similarity': 0.8249128919860628, 'reasonSegment': 1, 'message': '', 'commitId': '9bb55eef9d3d61beeba48186ff36cfd289a00152'},
 {'date': 'Wed Jun 26 14:41:18 2019 +0200', 'dataStamp': 1561552878.0, 'similarity': 0.8283464566929134, 'reasonSegment': 1, 'message': '', 'commitId': 'b05e372dfb92aab58fd10afe2d5c3a2a3432d924'},
 {'date': 'Wed Nov 13 15:11:33 2019 +0100', 'dataStamp': 1573654293.0, 'similarity': 0.826394344069128, 'reasonSegment': 1, 'message': '', 'commitId': '687b455d985b659491f6e77cd5c50a5952a84c6d'},
 {'date': 'Wed Nov 13 16:26:41 2019 +0100', 'dataStamp': 1573658801.0, 'similarity': 0.8283464566929134, 'reasonSegment': 1, 'message': '', 'commitId': '92d1406105237636f349c36cb0b489e5b23ea6af'},
 {'date': 'Thu Nov 14 11:59:35 2019 +0100', 'dataStamp': 1573729175.0, 'similarity': 0.8262910798122066, 'reasonSegment': 1, 'message': '', 'commitId': '67fe59c1eb57512c9786db5d79a120f47789cd22'},
 {'date': 'Thu Nov 14 14:47:35 2019 +0100', 'dataStamp': 1573739255.0, 'similarity': 0.8059135708870356, 'reasonSegment': 1, 'message': '', 'commitId': 'ec4c4090934c89f07e383cc0cb11fd6e70814ce6'},
 {'date': 'Thu Nov 14 15:42:25 2019 +0100', 'dataStamp': 1573742545.0, 'similarity': 0.8183925811437404, 'reasonSegment': 1, 'message': '', 'commitId': '7b28e2dedabbcf5e0ad8172e69a14a61027986ac'},
 {'date': 'Thu Nov 14 15:48:47 2019 +0100', 'dataStamp': 1573742927.0, 'similarity': 0.8190255220417634, 'reasonSegment': 1, 'message': '', 'commitId': '923f7f45c8c29ad224b2dda900aaaab28f436e73'},
 {'date': 'Fri Nov 15 11:14:40 2019 +0100', 'dataStamp': 1573812880.0, 'similarity': 0.8201550387596899, 'reasonSegment': 1, 'message': '', 'commitId': '6d91358796f53f04d4282ab1383373024046aa7d'},
 {'date': 'Mon Nov 18 14:46:38 2019 +0100', 'dataStamp': 1574084798.0, 'similarity': 0.8195197521301317, 'reasonSegment': 1, 'message': '', 'commitId': 'ff2dddc4421bebc6dedffcb80f6a4d983eff5ef7'},
 {'date': 'Mon Nov 18 16:00:17 2019 +0100', 'dataStamp': 1574089217.0, 'similarity': 0.8201550387596899, 'reasonSegment': 1, 'message': '', 'commitId': 'bb81d53eef1506db9e583fd8c3bf0b80e967089c'},
 {'date': 'Tue Nov 19 11:00:24 2019 +0100', 'dataStamp': 1574157624.0, 'similarity': 0.8294573643410853, 'reasonSegment': 0, 'message': '', 'commitId': '52b971a79e6e304bdbd4b3a26898a60fd1deed20'},
 {'date': 'Sun Nov 24 13:27:39 2019 +0100', 'dataStamp': 1574598459.0, 'similarity': 0.8046511627906977, 'reasonSegment': 0, 'message': '', 'commitId': '5815c6bebdb17e9770ba709243553eed8116522e'},
 {'date': 'Thu Dec 12 15:46:42 2019 +0530', 'dataStamp': 1576145802.0, 'similarity': 0.8395348837209302, 'reasonSegment': 0, 'message': '', 'commitId': '6d8fb006634689fd453f849d262c0f3561e25009'},
 {'date': 'Tue Jan 21 17:34:28 2020 +0100', 'dataStamp': 1579624468.0, 'similarity': 0.8120649651972158, 'reasonSegment': 1, 'message': '', 'commitId': 'ba81232f9b7ae3eb5927ec1ac4af3940e8d88931'},
 {'date': 'Mon Feb 10 12:32:24 2020 +0100', 'dataStamp': 1581334344.0, 'similarity': 0.8020108275328693, 'reasonSegment': 0, 'message': '', 'commitId': 'c3e8bfc3784a7f9b4364cfdf8f23cce76488bc30'},
 {'date': 'Mon Feb 10 12:36:22 2020 +0100', 'dataStamp': 1581334582.0, 'similarity': 0.8333333333333334, 'reasonSegment': 1, 'message': '', 'commitId': '10e82c5b33a2e09980520093fa0ddc06149c0983'},
 {'date': 'Tue Feb 25 14:34:26 2020 +0530', 'dataStamp': 1582621466.0, 'similarity': 0.8434108527131783, 'reasonSegment': 0, 'message': '', 'commitId': '8110d5ce07dcf1c6b0b2ad71a253a2ea221620f0'},
 {'date': 'Mon Mar 30 10:24:53 2020 +0200', 'dataStamp': 1585556693.0, 'similarity': 0.8159319412219644, 'reasonSegment': 1, 'message': '', 'commitId': 'fdd7a693913dc29dd17ce54fb099dd237760dedf'},
 {'date': 'Wed May 20 12:54:26 2020 +0530', 'dataStamp': 1589959466.0, 'similarity': 0.8074245939675174, 'reasonSegment': 0, 'message': '', 'commitId': 'c5bf66ea9db61dccc68605cc17f8d9fa2dc75ee3'},
 {'date': 'Fri May 22 13:46:17 2020 +0530', 'dataStamp': 1590135377.0, 'similarity': 0.8342328450269854, 'reasonSegment': 1, 'message': '', 'commitId': 'f4a11f5970c8c6b45cd85709191d19444d357de2'},
 {'date': 'Thu Jun 11 12:19:10 2020 -0300', 'dataStamp': 1591888750.0, 'similarity': 0.8317972350230415, 'reasonSegment': 1, 'message': '', 'commitId': '061bcda8117f823cbafd5e52e599ce7b28251b17'},
 {'date': 'Fri Jun 12 09:39:30 2020 -0300', 'dataStamp': 1591965570.0, 'similarity': 0.8317972350230415, 'reasonSegment': 1, 'message': '', 'commitId': '68cf6cf020baf57546a7cd6cae4474dd777a8f5e'},
 {'date': 'Tue Jun 16 13:23:56 2020 +0530', 'dataStamp': 1592294036.0, 'similarity': 0.804860088365243, 'reasonSegment': 1, 'message': '', 'commitId': '51f50e93bbf1f929dcbace1ca1cb23db13006588'},
 {'date': 'Mon Jun 22 14:16:55 2020 +0530', 'dataStamp': 1592815615.0, 'similarity': 0.841678939617084, 'reasonSegment': 0, 'message': '', 'commitId': 'c7df7768276042387a1d1d8744adf8ce1009212a'},
 {'date': 'Mon Jun 22 17:17:23 2020 +0200', 'dataStamp': 1592839043.0, 'similarity': 0.8188021228203184, 'reasonSegment': 1, 'message': '', 'commitId': 'b50dda0ae3565e4e728ec1199737ad0706de9858'},
 {'date': 'Mon Jun 22 17:21:21 2020 +0200', 'dataStamp': 1592839281.0, 'similarity': 0.8278999241849886, 'reasonSegment': 0, 'message': '', 'commitId': '86677ef94c19a7c01cf8fd70970ce9d0038295c9'},
 {'date': 'Mon Jun 29 11:29:16 2020 -0300', 'dataStamp': 1593440956.0, 'similarity': 0.8097043214556482, 'reasonSegment': 0, 'message': '', 'commitId': 'bfaffdcb2b6e5a9509b32dcf0896806a8d9ef6f9'},
 {'date': 'Mon Jun 29 11:56:04 2020 -0300', 'dataStamp': 1593442564.0, 'similarity': 0.8097043214556482, 'reasonSegment': 0, 'message': '', 'commitId': '0247b25b092566da51b1b227c022a78c692499a2'},
 {'date': 'Mon Jun 29 14:11:34 2020 -0300', 'dataStamp': 1593450694.0, 'similarity': 0.8188021228203184, 'reasonSegment': 0, 'message': '', 'commitId': '63fd7286e86be0a222759433b6076dd30a931967'},
 {'date': 'Mon Jun 29 14:17:17 2020 -0300', 'dataStamp': 1593451037.0, 'similarity': 0.8422597212032281, 'reasonSegment': 1, 'message': '', 'commitId': '4e6306c23212b9d6ae19b93ef0150c449c005704'},
 {'date': 'Thu Jul 2 10:03:16 2020 +0200', 'dataStamp': 1593676996.0, 'similarity': 0.8290535583272194, 'reasonSegment': 0, 'message': '', 'commitId': 'f9e7d2e20b64ec726f36c96251eee5570756315b'},
 {'date': 'Thu Jul 2 10:10:49 2020 +0200', 'dataStamp': 1593677449.0, 'similarity': 0.8373101952277657, 'reasonSegment': 1, 'message': '', 'commitId': 'a866e2f6deba16cdf16b960288bb3d64d07a61ac'},
 {'date': 'Wed Sep 2 15:49:22 2020 +0200', 'dataStamp': 1599054562.0, 'similarity': 0.8380332610267535, 'reasonSegment': 0, 'message': '', 'commitId': 'ab9b0b48fa3183d2e21297c94e82204ea37697bd'},
 {'date': 'Wed Sep 2 16:02:18 2020 +0200', 'dataStamp': 1599055338.0, 'similarity': 0.8380332610267535, 'reasonSegment': 0, 'message': '', 'commitId': '7ed2fdd8b2bb4392eb33031ddb4b2a265f4f1cd3'},
 {'date': 'Mon Sep 7 09:46:26 2020 +0200', 'dataStamp': 1599464786.0, 'similarity': 0.836587129428778, 'reasonSegment': 1, 'message': '', 'commitId': 'e0e322c90cb9e654d4ac8931c47fdfd58173fe97'},
 {'date': 'Mon Sep 7 09:47:25 2020 +0200', 'dataStamp': 1599464845.0, 'similarity': 0.8380332610267535, 'reasonSegment': 0, 'message': '', 'commitId': '09aac2e5fbd25edb3459ab457f8f7dde7a15b4fe'},
 {'date': 'Wed Sep 9 12:54:37 2020 +0200', 'dataStamp': 1599648877.0, 'similarity': 0.8344132469402448, 'reasonSegment': 1, 'message': '', 'commitId': 'bf7038f5851bae51828c83ce00d3b4496d4b2e2d'},
 {'date': 'Wed Sep 9 15:30:06 2020 +0200', 'dataStamp': 1599658206.0, 'similarity': 0.857451403887689, 'reasonSegment': 0, 'message': '', 'commitId': 'c1e6bd72d02e4afac820f9c3b7661829b3fc29b8'},
 {'date': 'Wed Sep 9 16:19:17 2020 +0200', 'dataStamp': 1599661157.0, 'similarity': 0.8596112311015118, 'reasonSegment': 0, 'message': '', 'commitId': 'ae877069d9ceb72dede91191a951f1ea2e8500ea'},
 {'date': 'Thu Sep 10 09:19:28 2020 +0200', 'dataStamp': 1599722368.0, 'similarity': 0.8596112311015118, 'reasonSegment': 0, 'message': '', 'commitId': '530b420a317d4d838d8e3954722f7434144c7ff8'},
 {'date': 'Thu Sep 10 09:24:33 2020 +0200', 'dataStamp': 1599722673.0, 'similarity': 0.8603311735061195, 'reasonSegment': 0, 'message': '', 'commitId': 'd8fb6c635c0bc3dd637e28fb6522977da389da4a'},
 {'date': 'Thu Sep 10 09:25:34 2020 +0200', 'dataStamp': 1599722734.0, 'similarity': 0.8600143575017947, 'reasonSegment': 1, 'message': '', 'commitId': '0883c8f5ea3cf763868f0fb531965700e8a79e14'},
 {'date': 'Thu Oct 8 10:59:49 2020 +0530', 'dataStamp': 1602134989.0, 'similarity': 0.8650394831299354, 'reasonSegment': 0, 'message': '', 'commitId': 'e71a16168080ad1d75039982006bbe71acdaa670'},
 {'date': 'Mon Dec 14 15:49:41 2020 +0100', 'dataStamp': 1607957381.0, 'similarity': 0.864321608040201, 'reasonSegment': 1, 'message': '', 'commitId': '0ba1f5c7314755f8255d9876afcd34c9f1a92557'},
 {'date': 'Mon Dec 14 15:50:07 2020 +0100', 'dataStamp': 1607957407.0, 'similarity': 0.8600143575017947, 'reasonSegment': 0, 'message': '', 'commitId': 'baeac7e47f00e75d734bef74fbc65efef6b414bd'},
 {'date': 'Thu Dec 17 16:31:04 2020 +0530', 'dataStamp': 1608202864.0, 'similarity': 0.8650394831299354, 'reasonSegment': 0, 'message': '', 'commitId': 'bd9878378e5522198c281fda916e05ecd9b9c3f1'},
 {'date': 'Wed Jul 7 12:32:10 2021 +0200', 'dataStamp': 1625653930.0, 'similarity': 0.8664752333094041, 'reasonSegment': 0, 'message': '', 'commitId': '4c1f9c8aed067408b32f0570c4218b595e4de8b3'},
 {'date': 'Wed Jul 7 13:02:28 2021 +0200', 'dataStamp': 1625655748.0, 'similarity': 0.8655221745350501, 'reasonSegment': 1, 'message': '', 'commitId': '61d54e19bba114019f7f7b94d5ccd7aa31c02c69'},
 {'date': 'Wed Jul 7 13:36:37 2021 +0200', 'dataStamp': 1625657797.0, 'similarity': 0.8648068669527897, 'reasonSegment': 0, 'message': '', 'commitId': 'a566f85a3bd21395bafc7cd76ba0b0b3b976e19a'},
 {'date': 'Wed Jul 7 13:37:14 2021 +0200', 'dataStamp': 1625657834.0, 'similarity': 0.8654259126700071, 'reasonSegment': 1, 'message': '', 'commitId': '0b5350de0df04c452c0179ea85a0d0b03fd8f1a7'},
 {'date': 'Wed Jul 14 16:21:00 2021 +0200', 'dataStamp': 1626272460.0, 'similarity': 0.8611309949892627, 'reasonSegment': 0, 'message': '', 'commitId': '877f75e7af8ae748c4d837cec4bcfc2bbcf426e3'},
 {'date': 'Thu Jul 15 09:04:38 2021 +0200', 'dataStamp': 1626332678.0, 'similarity': 0.8647482014388489, 'reasonSegment': 1, 'message': '', 'commitId': 'd22042b283a361929c52f35a666f3939f1bda541'},
 {'date': 'Tue Aug 31 13:40:44 2021 +0200', 'dataStamp': 1630410044.0, 'similarity': 0.854004252303331, 'reasonSegment': 1, 'message': '', 'commitId': 'f82286dd052d704d83fe9313dcefcb216275ba62'},
 {'date': 'Wed Sep 1 09:01:24 2021 +0200', 'dataStamp': 1630479684.0, 'similarity': 0.8546099290780141, 'reasonSegment': 1, 'message': '', 'commitId': '416df08c0805faf8d126f48620ad789d43a30041'},
 {'date': 'Fri Sep 3 08:36:09 2021 +0200', 'dataStamp': 1630650969.0, 'similarity': 0.8553191489361702, 'reasonSegment': 1, 'message': '', 'commitId': 'd0a078cd5c2cc508ed4d74cd8c646b918c1559cf'},
 {'date': 'Fri Sep 3 08:40:45 2021 +0200', 'dataStamp': 1630651245.0, 'similarity': 0.8666666666666667, 'reasonSegment': 0, 'message': '', 'commitId': 'd1e89dfc83c55a817c25373963c504c4cb939a0c'},
 {'date': 'Fri Sep 3 08:49:54 2021 +0200', 'dataStamp': 1630651794.0, 'similarity': 0.8666666666666667, 'reasonSegment': 0, 'message': '', 'commitId': '63d59b2e80ebb286ba684387ec86739a5ad498d6'},
 {'date': 'Fri Sep 3 11:31:05 2021 +0200', 'dataStamp': 1630661465.0, 'similarity': 0.8674269422665716, 'reasonSegment': 1, 'message': '', 'commitId': '2c1cb1169d717f202986f985458257e3916d84a8'},
 {'date': 'Fri Sep 3 11:31:54 2021 +0200', 'dataStamp': 1630661514.0, 'similarity': 0.8660014255167499, 'reasonSegment': 0, 'message': '', 'commitId': '241fdfee953c99b014944e0de620b56a1a1fae30'},
 {'date': 'Wed Dec 15 13:57:24 2021 +0100', 'dataStamp': 1639573044.0, 'similarity': 0.857448325017819, 'reasonSegment': 0, 'message': '', 'commitId': 'acfdb4c4432bc8e64e40d2c44c50da3724679b77'},
 {'date': 'Wed Dec 15 14:05:19 2021 +0100', 'dataStamp': 1639573519.0, 'similarity': 0.8634713144517067, 'reasonSegment': 1, 'message': '', 'commitId': 'd6f3f4e89f60aa4a4f7c0852573bd435adc211b2'},
 {'date': 'Wed Dec 15 14:09:11 2021 +0100', 'dataStamp': 1639573751.0, 'similarity': 0.8460421205519245, 'reasonSegment': 0, 'message': '', 'commitId': '33e9af8d6544f6a6ef513cf93d94b0f1dec94570'},
 {'date': 'Wed Dec 15 14:09:40 2021 +0100', 'dataStamp': 1639573780.0, 'similarity': 0.85949177877429, 'reasonSegment': 1, 'message': '', 'commitId': 'ec74c3e976f00153044b23d57cf65c3e0d779428'},
 {'date': 'Wed Jan 12 12:12:34 2022 +0100', 'dataStamp': 1641985954.0, 'similarity': 0.8609865470852018, 'reasonSegment': 0, 'message': '', 'commitId': 'ece9d626f9794b11ea5b99c3b0ae910aae5ce909'},
 {'date': 'Wed Jan 12 12:45:39 2022 +0100', 'dataStamp': 1641987939.0, 'similarity': 0.8609865470852018, 'reasonSegment': 0, 'message': '', 'commitId': '493d04ad64e4fde728b12dfd1e3434092fbeba2c'},
 {'date': 'Wed Jan 12 14:15:32 2022 +0100', 'dataStamp': 1641993332.0, 'similarity': 0.8609865470852018, 'reasonSegment': 0, 'message': '', 'commitId': '28b77b2286d8a5e7a2609789b73fd27fd6b02f0f'},
 {'date': 'Wed Jan 12 15:05:17 2022 +0100', 'dataStamp': 1641996317.0, 'similarity': 0.8609865470852018, 'reasonSegment': 0, 'message': '', 'commitId': 'bd94fc28eebe4038fcb3a8508af3fe09e4d49174'},
 {'date': 'Wed Jan 12 15:11:21 2022 +0100', 'dataStamp': 1641996681.0, 'similarity': 0.8609865470852018, 'reasonSegment': 0, 'message': '', 'commitId': '8d4ad5be96c186a678c4674be4e0f3e9cc63e2d0'},
 {'date': 'Wed Jan 12 15:20:16 2022 +0100', 'dataStamp': 1641997216.0, 'similarity': 0.8609865470852018, 'reasonSegment': 0, 'message': '', 'commitId': '6a6d2f58cc6d5fa9bd456dd7dac4655d901e7a76'},
 {'date': 'Thu Jan 13 10:02:40 2022 +0100', 'dataStamp': 1642064560.0, 'similarity': 0.8587443946188341, 'reasonSegment': 0, 'message': '', 'commitId': 'fa915a6e0bf1c981f924f7f3267cabea435e8c2d'},
 {'date': 'Thu Jan 13 10:09:36 2022 +0100', 'dataStamp': 1642064976.0, 'similarity': 0.8602391629297459, 'reasonSegment': 0, 'message': '', 'commitId': '1ed6baa5f24ad97974201dda1cbc5505f8c78579'},
 {'date': 'Mon Jan 17 09:58:56 2022 +0100', 'dataStamp': 1642409936.0, 'similarity': 0.8571428571428571, 'reasonSegment': 1, 'message': '', 'commitId': 'fde83197b2f1c6ed74d5b22d403e59984de71fa4'},
 {'date': 'Mon Jan 17 13:37:48 2022 +0100', 'dataStamp': 1642423068.0, 'similarity': 0.8617886178861789, 'reasonSegment': 1, 'message': '', 'commitId': '488bac5dec91926b78fda9133dfbff1e1c20d2b3'},
 {'date': 'Mon Jan 24 12:27:28 2022 +0100', 'dataStamp': 1643023648.0, 'similarity': 0.8577745025792188, 'reasonSegment': 1, 'message': '', 'commitId': '903e8151dcc6429d1c981dba0323a572b24f16fb'},
 {'date': 'Wed Feb 2 16:20:52 2022 +0100', 'dataStamp': 1643815252.0, 'similarity': 0.8548268238761975, 'reasonSegment': 0, 'message': '', 'commitId': '0b124746a667efe68c7dc1edd016070f035ee6b7'},
 {'date': 'Fri Feb 4 08:46:47 2022 +0100', 'dataStamp': 1643960807.0, 'similarity': 0.8455935906773488, 'reasonSegment': 1, 'message': '', 'commitId': '88e886bdb29b9c0240048ffd7f1c3e3a4823b24b'},
 {'date': 'Fri Feb 4 10:19:36 2022 +0100', 'dataStamp': 1643966376.0, 'similarity': 0.8450909090909091, 'reasonSegment': 1, 'message': '', 'commitId': '666119a7e5a59d403161b6981fffede98954f81e'},
 {'date': 'Fri Feb 4 10:19:43 2022 +0100', 'dataStamp': 1643966383.0, 'similarity': 0.8438634713144517, 'reasonSegment': 1, 'message': '', 'commitId': '468a6bb718559bcc6d9fadb5dd42640a27146917'},
 {'date': 'Fri Feb 4 10:27:41 2022 +0100', 'dataStamp': 1643966861.0, 'similarity': 0.8433647570703409, 'reasonSegment': 1, 'message': '', 'commitId': 'b2b2ce03989cb191f5dcf9a6b79f95ae21ae208c'},
 {'date': 'Fri Mar 25 10:53:55 2022 +0100', 'dataStamp': 1648202035.0, 'similarity': 0.8448150833937635, 'reasonSegment': 0, 'message': '', 'commitId': 'e7400e8b454462a8fcfa85afafcc5c08ca3417c9'},
 {'date': 'Fri Mar 25 13:01:28 2022 +0100', 'dataStamp': 1648209688.0, 'similarity': 0.8437047756874095, 'reasonSegment': 1, 'message': '', 'commitId': '9342dac6fd15f440cf84500263103e9bd9abdfbe'},
 {'date': 'Fri Mar 25 13:09:23 2022 +0100', 'dataStamp': 1648210163.0, 'similarity': 0.8472727272727273, 'reasonSegment': 1, 'message': '', 'commitId': '6d5dad60bdf0c7eb5ae0d4748bf15f9b9290e20a'},
 {'date': 'Fri Mar 25 13:17:52 2022 +0100', 'dataStamp': 1648210672.0, 'similarity': 0.846656976744186, 'reasonSegment': 1, 'message': '', 'commitId': '15b9b8adf4cf20789ef8517dc55f32838e5cf1ba'},
 {'date': 'Mon Mar 28 08:49:39 2022 +0200', 'dataStamp': 1648450179.0, 'similarity': 0.8518248175182481, 'reasonSegment': 1, 'message': '', 'commitId': '6caad67a7332b42e55e1cc5714d1439d4b8e0e1a'},
 {'date': 'Mon Mar 28 08:54:22 2022 +0200', 'dataStamp': 1648450462.0, 'similarity': 0.852014652014652, 'reasonSegment': 1, 'message': '', 'commitId': '952c189ae691de7fff0222aab35afa7faccf2060'},
 {'date': 'Fri May 27 14:14:20 2022 +0200', 'dataStamp': 1653653660.0, 'similarity': 0.8556776556776556, 'reasonSegment': 0, 'message': '', 'commitId': 'c7e7e223a6904ee01c3ed8116c50dbc05b98d0f0'},
 {'date': 'Mon May 30 11:15:52 2022 +0200', 'dataStamp': 1653902152.0, 'similarity': 0.8537291817523533, 'reasonSegment': 1, 'message': '', 'commitId': '58d6e6078c0d3319c60d9ebcbffe30291c353ff1'},
 {'date': 'Thu Jul 7 10:22:46 2022 +0200', 'dataStamp': 1657182166.0, 'similarity': 0.8544532947139754, 'reasonSegment': 0, 'message': '', 'commitId': 'c8a55c6ab2275aac46c4c47f38034dc342ba855a'},
 {'date': 'Thu Jul 7 10:31:39 2022 +0200', 'dataStamp': 1657182699.0, 'similarity': 0.8540462427745664, 'reasonSegment': 1, 'message': '', 'commitId': 'bb63f52d8c5a9229567acaa75b5eff8f1bc236d4'},
 {'date': 'Wed Sep 27 10:10:06 2023 +0200', 'dataStamp': 1695802206.0, 'similarity': 0.8497109826589595, 'reasonSegment': 0, 'message': '', 'commitId': 'a3eaaadc77b8c41813d6d087299924c8308a963e'},
 {'date': 'Tue Oct 3 16:32:41 2023 +0200', 'dataStamp': 1696343561.0, 'similarity': 0.8562138728323699, 'reasonSegment': 0, 'message': '', 'commitId': '497c5348aee3118e8bcf7384262e5ce426c90d45'},
 {'date': 'Wed Oct 4 09:14:14 2023 +0200', 'dataStamp': 1696403654.0, 'similarity': 0.8551971326164874, 'reasonSegment': 1, 'message': '', 'commitId': 'ff334831a8f15f2df0db5245f1ec243fa335647c'},
 {'date': 'Wed Oct 4 09:32:31 2023 +0200', 'dataStamp': 1696404751.0, 'similarity': 0.8524118070554355, 'reasonSegment': 1, 'message': '', 'commitId': '492883b7b6e8bacfdbf19542c2199a0b246d453d'},
 {'date': 'Wed Oct 4 09:32:59 2023 +0200', 'dataStamp': 1696404779.0, 'similarity': 0.8538516918646508, 'reasonSegment': 0, 'message': '', 'commitId': '30a53502eb43f643c9b8f260a2e2b3d445ccf47b'},
 {'date': 'Wed Oct 4 09:34:18 2023 +0200', 'dataStamp': 1696404858.0, 'similarity': 0.8560115190784737, 'reasonSegment': 0, 'message': '', 'commitId': '075c828155bbf9c916c691f6f7b386611e8590d9'},
 {'date': 'Wed Oct 4 09:36:51 2023 +0200', 'dataStamp': 1696405011.0, 'similarity': 0.8516918646508279, 'reasonSegment': 0, 'message': '', 'commitId': 'bfab30f482db15e1258853bcd4c510a7454ca9ee'},
 {'date': 'Wed Oct 4 11:25:49 2023 +0200', 'dataStamp': 1696411549.0, 'similarity': 0.8516918646508279, 'reasonSegment': 0, 'message': '', 'commitId': '028e3d50ab30cb892740adfa3631ec44862411d0'},
 {'date': 'Wed Oct 4 11:28:17 2023 +0200', 'dataStamp': 1696411697.0, 'similarity': 0.8516918646508279, 'reasonSegment': 1, 'message': '', 'commitId': '8145f58e434f72a39459be52b936affa18382c40'},
 {'date': 'Wed Oct 11 16:15:46 2023 +0200', 'dataStamp': 1697033746.0, 'similarity': 0.8464285714285714, 'reasonSegment': 1, 'message': '', 'commitId': '9c67e676734183f9730a504da97ecd117c01ebba'},
 {'date': 'Wed Oct 18 10:20:27 2023 +0200', 'dataStamp': 1697617227.0, 'similarity': 0.8464285714285714, 'reasonSegment': 1, 'message': '', 'commitId': '237bf6786d8eeec91309ed4437983104021b36e8'},
 {'date': 'Wed Oct 18 10:31:43 2023 +0200', 'dataStamp': 1697617903.0, 'similarity': 0.8464285714285714, 'reasonSegment': 0, 'message': '', 'commitId': 'a29ef3d1ecc4f687f5db7827a59b913608cd2130'},
 {'date': 'Mon Oct 23 10:47:38 2023 +0200', 'dataStamp': 1698050858.0, 'similarity': 0.8460441910192444, 'reasonSegment': 1, 'message': '', 'commitId': '113eb5020ea0e24fd443965e1d9f70ee49559b71'},
 {'date': 'Mon Oct 23 10:57:45 2023 +0200', 'dataStamp': 1698051465.0, 'similarity': 0.8460441910192444, 'reasonSegment': 1, 'message': '', 'commitId': '165d2909618ae2a44400dbe1c387a837d8c006dd'},
 {'date': 'Mon Nov 6 14:12:44 2023 +0100', 'dataStamp': 1699276364.0, 'similarity': 0.78748370273794, 'reasonSegment': 0, 'message': '', 'commitId': 'e9a85d35b518d5dea50e6bc2ca7c990c5d4c568a'},
 {'date': 'Mon Nov 6 17:11:26 2023 +0100', 'dataStamp': 1699287086.0, 'similarity': 0.8106111484217595, 'reasonSegment': 0, 'message': '', 'commitId': 'd4cad75170a39e45804d202b31d7d5aaf7fc9111'},
 {'date': 'Tue Nov 7 11:00:51 2023 +0100', 'dataStamp': 1699351251.0, 'similarity': 0.8089812332439679, 'reasonSegment': 0, 'message': '', 'commitId': '3bcfdf3e3e29a19382cd3d1df2ced7369cf514d0'},
 {'date': 'Mon Nov 13 12:20:59 2023 +0100', 'dataStamp': 1699874459.0, 'similarity': 0.8166441136671178, 'reasonSegment': 0, 'message': '', 'commitId': '50b1a9b326149d479d8b5b32b9b06ad7f9d59fe3'},
 {'date': 'Mon Nov 13 12:26:28 2023 +0100', 'dataStamp': 1699874788.0, 'similarity': 0.8171970209884902, 'reasonSegment': 0, 'message': '', 'commitId': 'a1b1e7adb31d29cca1b6a7a89de9c93b3e8552c5'},
 {'date': 'Mon Nov 13 15:16:14 2023 +0100', 'dataStamp': 1699884974.0, 'similarity': 0.7969776609724047, 'reasonSegment': 0, 'message': '', 'commitId': '961e8571cf883d62edd00a0a4a9e2c62a71b74b3'},
 {'date': 'Tue Nov 14 10:18:15 2023 +0100', 'dataStamp': 1699953495.0, 'similarity': 0.793848167539267, 'reasonSegment': 0, 'message': '', 'commitId': '47fa9972c16abb08605825f70a48d738861ab47a'},
 {'date': 'Fri Nov 17 10:50:23 2023 +0100', 'dataStamp': 1700214623.0, 'similarity': 0.7638539042821159, 'reasonSegment': 0, 'message': '', 'commitId': '880b0dd436e5d1bd690b84994fc989c3a0d1a093'},
 {'date': 'Fri Nov 17 12:18:28 2023 +0100', 'dataStamp': 1700219908.0, 'similarity': 0.7797045600513809, 'reasonSegment': 0, 'message': '', 'commitId': '5274192f92fdad946dbe759910b8c455a1587ba9'},
 {'date': 'Mon Nov 20 09:21:37 2023 +0100', 'dataStamp': 1700468497.0, 'similarity': 0.7792041078305519, 'reasonSegment': 0, 'message': '', 'commitId': '6423fe43ebb41d80b1c21391c81c7c13f678a6ab'},
 {'date': 'Mon Nov 20 09:55:03 2023 +0100', 'dataStamp': 1700470503.0, 'similarity': 0.7711757269279393, 'reasonSegment': 0, 'message': '', 'commitId': '17da4d1d5f8eb3b229b5c504d035478075ab7f57'},
 {'date': 'Mon Nov 20 09:56:05 2023 +0100', 'dataStamp': 1700470565.0, 'similarity': 0.7682619647355163, 'reasonSegment': 0, 'message': '', 'commitId': '4e16b7c09fc3b4e50fc66bdce2632e25cabe2c6f'},
 {'date': 'Wed Nov 29 11:38:25 2023 +0100', 'dataStamp': 1701254305.0, 'similarity': 0.7668133249528598, 'reasonSegment': 0, 'message': '', 'commitId': '048bb6238b6297e9f6095ba49281605de05331eb'}]


# Erlang
# data = [{'date': 'Sat May 22 03:06:00 2021 +0900', 'dataStamp': 1621620360.0, 'similarity': 0.9936165968481947, 'reasonSegment': 0, 'message': '', 'commitId': '789fe8333a0ef776b0d115365c1d4213377571be'},
#  {'date': 'Mon Jun 28 15:17:21 2021 +0800', 'dataStamp': 1624864641.0, 'similarity': 0.9936165968481947, 'reasonSegment': 1, 'message': '1: Clone Generated.', 'commitId': 'c63bdc355a444f637edeac874778f80a9896685f',"offset_x": -100, "offset_y": 0.08},
#  {'date': 'Mon Jun 28 18:40:04 2021 +0800', 'dataStamp': 1624876804.0, 'similarity': 0.9936165968481947, 'reasonSegment': 1, 'message': '', 'commitId': 'e1b0f44a8a00ac6b8abaaa432b1dee3dc63df2c7'},
#  {'date': 'Tue Jul 6 18:26:54 2021 +0800', 'dataStamp': 1625567214.0, 'similarity': 0.9639357114856919, 'reasonSegment': 1, 'message': '', 'commitId': '5efd5c8d3b17e54c5687050bba117c635471886b'},
#  {'date': 'Tue Jul 6 18:36:40 2021 +0800', 'dataStamp': 1625567800.0, 'similarity': 0.9639074146724206, 'reasonSegment': 1, 'message': '', 'commitId': '7c0fd642bb3573ed6e3eedd4b4aa9223db12c635'},
#  {'date': 'Wed Jul 7 19:15:35 2021 +0800', 'dataStamp': 1625656535.0, 'similarity': 0.9635151039623382, 'reasonSegment': 1, 'message': '', 'commitId': '477097c06261d7b2edaf4eddeded52b4eb7d8749'},
#  {'date': 'Fri Jul 9 15:38:51 2021 +0800', 'dataStamp': 1625816331.0, 'similarity': 0.9620054837446141, 'reasonSegment': 1, 'message': '', 'commitId': '14af90d0c3ea4c319d920e16f2012af9e988658e'},
#  {'date': 'Sat Jul 10 14:29:45 2021 +0800', 'dataStamp': 1625898585.0, 'similarity': 0.9620054837446141, 'reasonSegment': 1, 'message': '', 'commitId': '4c122d07220d7adb4a266b499f0b6045567d79d3'},
#  {'date': 'Tue Jul 13 16:38:06 2021 +0800', 'dataStamp': 1626165486.0, 'similarity': 0.9574965880288555, 'reasonSegment': 1, 'message': '', 'commitId': '871353704ab0010cf949f21eb60d3b19a82f11da'},
#  {'date': 'Wed Jul 14 16:53:52 2021 +0800', 'dataStamp': 1626252832.0, 'similarity': 0.9737158908507223, 'reasonSegment': 1, 'message': '', 'commitId': '6a8e35ce3ae909e0b1eaa49fe387e6b626fee935'},
#  {'date': 'Thu Jul 15 11:36:49 2021 +0800', 'dataStamp': 1626320209.0, 'similarity': 0.9723668402082499, 'reasonSegment': 1, 'message': '', 'commitId': 'beecc4c5a22a4533cc9764eeff05c3c98a3d4be3'},
#  {'date': 'Thu Jul 15 11:56:13 2021 +0800', 'dataStamp': 1626321373.0, 'similarity': 0.9567672833495618, 'reasonSegment': 1, 'message': '', 'commitId': '4da59a57859ad9c12e6584edb132174a672b9f8d'},
#  {'date': 'Thu Jul 15 18:44:56 2021 +0800', 'dataStamp': 1626345896.0, 'similarity': 0.936278342455043, 'reasonSegment': 1, 'message': '', 'commitId': 'ba166967c982ae95155d1af7520cb219fb8b9601'},
#  {'date': 'Thu Jul 15 18:54:31 2021 +0800', 'dataStamp': 1626346471.0, 'similarity': 0.936278342455043, 'reasonSegment': 1, 'message': '', 'commitId': 'a1488b39461c55f835ab3a774e1a84e491775126'},
#  {'date': 'Mon Jul 19 14:57:47 2021 +0800', 'dataStamp': 1626677867.0, 'similarity': 0.9375611665688002, 'reasonSegment': 1, 'message': '', 'commitId': 'e6424d63d896b06510ab5b81f4875d6a700c3219'},
#  {'date': 'Mon Jul 19 15:36:00 2021 +0800', 'dataStamp': 1626680160.0, 'similarity': 0.9440394088669951, 'reasonSegment': 1, 'message': '', 'commitId': '2898e9c6dc7c9d0b5ffa21dde6b69efa70c56c26'},
#  {'date': 'Tue Jul 20 09:56:05 2021 +0800', 'dataStamp': 1626746165.0, 'similarity': 0.9445977917981072, 'reasonSegment': 1, 'message': '', 'commitId': 'af5470cb303f6e3b3f2089b611ee34e5825de09f'},
#  {'date': 'Tue Jul 20 10:02:55 2021 +0800', 'dataStamp': 1626746575.0, 'similarity': 0.94796201028888, 'reasonSegment': 1, 'message': '', 'commitId': '98c7f9edb21dc00981ee78aebcdf9b5d46010db2'},
#  {'date': 'Fri Jul 23 11:15:05 2021 +0800', 'dataStamp': 1627010105.0, 'similarity': 0.9479414093428346, 'reasonSegment': 1, 'message': '', 'commitId': '93e12570458b9ed150a7c899f9aac70fe4633f91'},
#  {'date': 'Fri Jul 23 13:42:59 2021 +0800', 'dataStamp': 1627018979.0, 'similarity': 0.9479207920792079, 'reasonSegment': 1, 'message': '', 'commitId': '684e46c45da3d0b40ba9a38d73227f1c42096c5b'},
#  {'date': 'Fri Jul 23 14:11:32 2021 +0800', 'dataStamp': 1627020692.0, 'similarity': 0.9479001584786054, 'reasonSegment': 1, 'message': '', 'commitId': '0704cbc986c37ff507d39c9e9ff953ef76a17767'},
#  {'date': 'Fri Jul 23 15:13:44 2021 +0800', 'dataStamp': 1627024424.0, 'similarity': 0.9479207920792079, 'reasonSegment': 1, 'message': '', 'commitId': '14da1084432c5cd4daedc1a75d5bd680ffbf9285'},
#  {'date': 'Fri Jul 23 17:10:39 2021 +0800', 'dataStamp': 1627031439.0, 'similarity': 0.9475351415561275, 'reasonSegment': 1, 'message': '', 'commitId': '4b50bfb4c2052353a40982d4ed7023d5e06a6647'},
#  {'date': 'Fri Jul 23 18:46:07 2021 +0800', 'dataStamp': 1627037167.0, 'similarity': 0.9435755295980994, 'reasonSegment': 1, 'message': '', 'commitId': '4c5b75f2815fc58a9719b7f8c21c705a3b1f1450'},
#  {'date': 'Sat Jul 31 18:52:05 2021 +0200', 'dataStamp': 1627750325.0, 'similarity': 0.9437512378688849, 'reasonSegment': 1, 'message': '', 'commitId': '5d59ac1f023c409ceaa43297d9ed16fc87e73bd3'},
#  {'date': 'Fri Aug 13 10:32:31 2021 +0800', 'dataStamp': 1628821951.0, 'similarity': 0.9391013007489161, 'reasonSegment': 1, 'message': '', 'commitId': 'e6f9767066ebc651ea3de40543fd943b541971a3'},
#  {'date': 'Mon Aug 16 15:07:42 2021 +0800', 'dataStamp': 1629097662.0, 'similarity': 0.9436342136381553, 'reasonSegment': 0, 'message': '', 'commitId': '589951c637441c137c3648252686f30f67f2bbb5'},
#  {'date': 'Thu Aug 19 09:23:38 2021 +0800', 'dataStamp': 1629336218.0, 'similarity': 0.9431102362204724, 'reasonSegment': 1, 'message': '', 'commitId': '178d1006e1788ad8c04932d3b9e0e8b44d3f331a'},
#  {'date': 'Thu Aug 19 10:27:32 2021 +0800', 'dataStamp': 1629340052.0, 'similarity': 0.9471287128712871, 'reasonSegment': 1, 'message': '', 'commitId': '5652917af6fd4cbe9016cac85c7f1159097caa1e'},
#  {'date': 'Thu Aug 19 11:43:00 2021 +0800', 'dataStamp': 1629344580.0, 'similarity': 0.9485702938840349, 'reasonSegment': 1, 'message': '', 'commitId': '1886aa8bff3924ca8301221f26380d94b8ffe695'},
#  {'date': 'Wed Aug 25 16:37:05 2021 +0800', 'dataStamp': 1629880625.0, 'similarity': 0.9481834425253127, 'reasonSegment': 1, 'message': '', 'commitId': 'cc56c74964e3d4ce7f69bc4f2211ee4c5ac91fff'},
#  {'date': 'Wed Aug 25 18:05:13 2021 +0800', 'dataStamp': 1629885913.0, 'similarity': 0.9476190476190476, 'reasonSegment': 1, 'message': '', 'commitId': '4ea451e2075bbb10c71d174fec6cf3b4fd3d4217'},
#  {'date': 'Mon Aug 30 10:32:28 2021 +0200', 'dataStamp': 1630312348.0, 'similarity': 0.9200079792539397, 'reasonSegment': 1, 'message': '', 'commitId': '24e870672ce19fba617af0672bcfbfac775484c1'},
#  {'date': 'Wed Sep 8 09:46:47 2021 +0800', 'dataStamp': 1631065607.0, 'similarity': 0.9474310652648285, 'reasonSegment': 1, 'message': '', 'commitId': 'be38bcc5ccccc2a7a421506c6c4de33c8f1c9531'},
#  {'date': 'Wed Sep 8 09:53:39 2021 +0800', 'dataStamp': 1631066019.0, 'similarity': 0.9474310652648285, 'reasonSegment': 1, 'message': '', 'commitId': '8531e9ce11b720ec85a3c7c62c74d9d695da3746'},
#  {'date': 'Wed Sep 8 10:58:00 2021 +0800', 'dataStamp': 1631069880.0, 'similarity': 0.947827811942075, 'reasonSegment': 1, 'message': '', 'commitId': '29cad91a471526af5540bd42c5763acb28a2519a'},
#  {'date': 'Wed Sep 29 13:36:30 2021 +0800', 'dataStamp': 1632893790.0, 'similarity': 0.9253939756632755, 'reasonSegment': 1, 'message': '', 'commitId': 'fe5a169be16f16ae4bcddc7f0d5eb93385dd88a8'},
#  {'date': 'Fri Oct 1 14:45:31 2021 +0200', 'dataStamp': 1633092331.0, 'similarity': 0.9456306840648477, 'reasonSegment': 1, 'message': '', 'commitId': 'e9710ade14d28d541e45dc3f88c2a52136b92670'},
#  {'date': 'Mon Oct 4 12:00:32 2021 +0200', 'dataStamp': 1633341632.0, 'similarity': 0.9463684939639818, 'reasonSegment': 1, 'message': '', 'commitId': '9304e3c122e14357db87e3afe0a719a105506996'},
#  {'date': 'Thu Oct 7 09:23:20 2021 +0200', 'dataStamp': 1633591400.0, 'similarity': 0.9076802199960715, 'reasonSegment': 1, 'message': '', 'commitId': '7b394267dd72e988a8c5d746dd64783e4fe67f97'},
#  {'date': 'Mon Oct 11 01:35:43 2021 +0200', 'dataStamp': 1633908943.0, 'similarity': 0.9255934570117694, 'reasonSegment': 1, 'message': '', 'commitId': '71731c01f1b69b58ca5423c00d70845363b7b2a1'},
#  {'date': 'Thu Oct 14 10:00:01 2021 +0200', 'dataStamp': 1634198401.0, 'similarity': 0.926391382405745, 'reasonSegment': 1, 'message': '', 'commitId': 'dcca1d75444056ac29230ff389773a7035c26750'},
#  {'date': 'Tue Oct 19 16:00:37 2021 +0200', 'dataStamp': 1634652037.0, 'similarity': 0.9078585461689588, 'reasonSegment': 1, 'message': '', 'commitId': 'ec429857e07e82d61f0e08598fc82ddc46bcbfa1'},
#  {'date': 'Wed Oct 27 14:09:08 2021 +0200', 'dataStamp': 1635336548.0, 'similarity': 0.9062377402903099, 'reasonSegment': 1, 'message': '', 'commitId': '7ae6e04582f856c220d93b18e6665264010fa42e'},
#  {'date': 'Tue Nov 2 09:27:50 2021 +0100', 'dataStamp': 1635841670.0, 'similarity': 0.906256128652677, 'reasonSegment': 1, 'message': '', 'commitId': '8385eff98ebe0a85ff145bfb826fe9e17990e9ee'},
#  {'date': 'Mon Nov 8 15:46:49 2021 -0300', 'dataStamp': 1636397209.0, 'similarity': 0.9044822861616755, 'reasonSegment': 1, 'message': '', 'commitId': '8fe342a02dd1531b713377abca25b8e92d833cbe'},
#  {'date': 'Mon Nov 8 17:50:58 2021 -0300', 'dataStamp': 1636404658.0, 'similarity': 0.9044822861616755, 'reasonSegment': 1, 'message': '', 'commitId': '60d5017eea3e13311c0707484755392e7c48fbc8'},
#  {'date': 'Tue Nov 9 23:20:30 2021 +0100', 'dataStamp': 1636496430.0, 'similarity': 0.9038950871011939, 'reasonSegment': 1, 'message': '', 'commitId': 'c89a663b5315c7e9d62d1ae1b711233970b6d145'},
#  {'date': 'Thu Nov 18 10:56:58 2021 +0800', 'dataStamp': 1637204218.0, 'similarity': 0.8959907030796049, 'reasonSegment': 1, 'message': '', 'commitId': '33f5eec802bbfd6772cb72778f30207eb5a300df'},
#  {'date': 'Tue Nov 23 13:49:12 2021 +0800', 'dataStamp': 1637646552.0, 'similarity': 0.8953780700058016, 'reasonSegment': 1, 'message': '', 'commitId': 'ef0e440d27f5fa79937cdd6202e27d49c9ddcb4d'},
#  {'date': 'Tue Nov 23 16:39:06 2021 +0100', 'dataStamp': 1637681946.0, 'similarity': 0.894797911429124, 'reasonSegment': 1, 'message': '', 'commitId': 'fda2e861870cf5d634d48dacadb9b02a283fba9e'},
#  {'date': 'Tue Dec 7 14:07:40 2021 +0100', 'dataStamp': 1638882460.0, 'similarity': 0.894797911429124, 'reasonSegment': 1, 'message': '', 'commitId': 'e6ecc6ca60f274c421dae77c97166ebdff39af6c'},
#  {'date': 'Tue Dec 7 15:42:17 2021 +0100', 'dataStamp': 1638888137.0, 'similarity': 0.8942177528524463, 'reasonSegment': 1, 'message': '', 'commitId': '5440b431a12d7df1c21fc172e8a64a32fb25f4bd'},
#  {'date': 'Tue Dec 7 16:14:32 2021 +0100', 'dataStamp': 1638890072.0, 'similarity': 0.8941062801932367, 'reasonSegment': 1, 'message': '', 'commitId': '14bef1ba312c0260131a8017748c166cffdc8eb1'},
#  {'date': 'Mon Dec 6 22:50:42 2021 +0300', 'dataStamp': 1638820242.0, 'similarity': 0.894604525236898, 'reasonSegment': 1, 'message': '', 'commitId': '2b0a3e8ba3665dc9455aae7c4c31d01f5c14faf5'},
#  {'date': 'Wed Dec 8 11:00:46 2021 +0100', 'dataStamp': 1638957646.0, 'similarity': 0.8935265700483092, 'reasonSegment': 1, 'message': '', 'commitId': '92f116afa4d5563ce5af70668e6510fde1690248'},
#  {'date': 'Wed Dec 8 15:15:27 2021 -0300', 'dataStamp': 1638987327.0, 'similarity': 0.8943907156673114, 'reasonSegment': 1, 'message': '', 'commitId': '2b5fe9179ef4cb4f9cfe0e325a63ff341b4a3367'},
#  {'date': 'Fri Dec 10 00:46:11 2021 +0800', 'dataStamp': 1639068371.0, 'similarity': 0.8902415458937198, 'reasonSegment': 1, 'message': '', 'commitId': '8493b61cb5510a8057427014d4bff6b7db150025'},
#  {'date': 'Tue Dec 14 16:21:02 2021 +0300', 'dataStamp': 1639488062.0, 'similarity': 0.890048309178744, 'reasonSegment': 1, 'message': '', 'commitId': 'b8a68d7a9ff2b7967f53c836ac9605b19e13b109'},
#  {'date': 'Fri Dec 17 17:19:40 2021 +0100', 'dataStamp': 1639757980.0, 'similarity': 0.8894899536321483, 'reasonSegment': 1, 'message': '', 'commitId': 'ca2660d60977d949aa6ee3312719070543ff47e7'},
#  {'date': 'Mon Dec 20 14:22:06 2021 +0800', 'dataStamp': 1639981326.0, 'similarity': 0.8898337843061461, 'reasonSegment': 1, 'message': '', 'commitId': '52502e29c34592809daf3cc44d28f033796a6e8b'},
#  {'date': 'Mon Dec 27 09:13:24 2021 +0800', 'dataStamp': 1640567604.0, 'similarity': 0.8892753623188406, 'reasonSegment': 1, 'message': '', 'commitId': '523b5761b726ef64367c821d31f2044b8f3b5176'},
#  {'date': 'Mon Dec 20 09:23:00 2021 +0800', 'dataStamp': 1639963380.0, 'similarity': 0.8903500290079288, 'reasonSegment': 1, 'message': '', 'commitId': '668180388c08c6655358cb92a0f9a7216e6f2907'},
#  {'date': 'Tue Dec 28 23:46:22 2021 +0800', 'dataStamp': 1640706382.0, 'similarity': 0.8900057993427412, 'reasonSegment': 1, 'message': '', 'commitId': '4b6bba11eb3ddec8fbd64745f44b0bc9f42035d5'},
#  {'date': 'Wed Dec 29 12:49:56 2021 +0800', 'dataStamp': 1640753396.0, 'similarity': 0.8883747831116252, 'reasonSegment': 1, 'message': '', 'commitId': '121d90699244dd33b5731f64d0f4d1224f541766'},
#  {'date': 'Wed Dec 29 22:33:34 2021 +0800', 'dataStamp': 1640788414.0, 'similarity': 0.8888674512830407, 'reasonSegment': 1, 'message': '', 'commitId': 'b8bb5ff738704ace0f5c6266e1f74b819c10fe53'},
#  {'date': 'Mon Jan 3 11:39:06 2022 +0100', 'dataStamp': 1641206346.0, 'similarity': 0.8886530297182555, 'reasonSegment': 1, 'message': '', 'commitId': '2898fa76e1affcc3315abee98aac35d6d1312115'},
#  {'date': 'Wed Jan 5 20:37:08 2022 +0100', 'dataStamp': 1641411428.0, 'similarity': 0.8886530297182555, 'reasonSegment': 1, 'message': '', 'commitId': '63167cea70e275425ed3f0b51f2eccc89299c67a'},
#  {'date': 'Fri Jan 7 16:30:56 2022 +0800', 'dataStamp': 1641544256.0, 'similarity': 0.8884600540331918, 'reasonSegment': 0, 'message': '', 'commitId': '8d261261736d775c699fdbb6fcd28f5fc8a936d4'},
#  {'date': 'Thu Jan 27 18:57:35 2022 +0800', 'dataStamp': 1643281055.0, 'similarity': 0.8876036244457297, 'reasonSegment': 1, 'message': '', 'commitId': 'a7676d0163dfbfae23ce6c2c07c6bf2b51da1ce2'},
#  {'date': 'Tue Feb 8 11:07:03 2022 +0800', 'dataStamp': 1644289623.0, 'similarity': 0.8828379674017258, 'reasonSegment': 1, 'message': '', 'commitId': '06168f708009c7fe948c1f1979c67b22c7f47426'},
#  {'date': 'Thu Feb 10 16:23:54 2022 -0300', 'dataStamp': 1644521034.0, 'similarity': 0.8828379674017258, 'reasonSegment': 1, 'message': '', 'commitId': '609d8a5efa561e664da56d5334d4c183d9d29688'},
#  {'date': 'Thu Feb 10 14:19:33 2022 +0800', 'dataStamp': 1644473973.0, 'similarity': 0.8770460601446517, 'reasonSegment': 1, 'message': '', 'commitId': '0826084ce9994d2b68fa7fbc0e954b2b7afd510f'},
#  {'date': 'Fri Feb 11 11:14:56 2022 +0800', 'dataStamp': 1644549296.0, 'similarity': 0.8770460601446517, 'reasonSegment': 1, 'message': '', 'commitId': 'fbefc9217856cf331ea367affaf119bbd770c859'},
#  {'date': 'Tue Feb 22 10:50:49 2022 +0800', 'dataStamp': 1645498249.0, 'similarity': 0.8762122076440388, 'reasonSegment': 1, 'message': '', 'commitId': '437feefdc0a963b554c1b63d1daf3897374141e3'},
#  {'date': 'Tue Mar 15 11:55:47 2022 +0800', 'dataStamp': 1647316547.0, 'similarity': 0.8741935483870967, 'reasonSegment': 1, 'message': '', 'commitId': '87a29beb5fdcdb43d861831d221b4a99037d0457'},
#  {'date': 'Tue Mar 15 18:52:45 2022 +0800', 'dataStamp': 1647341565.0, 'similarity': 0.8703948611373512, 'reasonSegment': 1, 'message': '', 'commitId': 'df74c180b719c192475ca4c8f19fea04c5bf3556'},
#  {'date': 'Mon Mar 21 16:51:31 2022 +0100', 'dataStamp': 1647877891.0, 'similarity': 0.8762122076440388, 'reasonSegment': 1, 'message': '', 'commitId': '91bcf02970bd1fe0dfe06744a24aa8a149ac0052'},
#  {'date': 'Tue Mar 22 15:27:10 2022 +0800', 'dataStamp': 1647934030.0, 'similarity': 0.8703458703458703, 'reasonSegment': 1, 'message': '', 'commitId': '97c05d3a7252ef98a65e830df9bb5d17e0c55aa3'},
#  {'date': 'Fri Apr 22 15:53:39 2022 +0300', 'dataStamp': 1650632019.0, 'similarity': 0.8687535357344899, 'reasonSegment': 1, 'message': '', 'commitId': 'fc2ea9e484f2bd2b62f8be2b55a7c74799fa5485'},
#  {'date': 'Thu May 5 10:30:59 2022 +0800', 'dataStamp': 1651717859.0, 'similarity': 0.8660529776441857, 'reasonSegment': 1, 'message': '', 'commitId': '2987bd47ad4da86535cdcb7cd9b528ca24be4ea6'},
#  {'date': 'Wed Jun 15 16:50:05 2022 +0300', 'dataStamp': 1655301005.0, 'similarity': 0.8649155722326454, 'reasonSegment': 1, 'message': '', 'commitId': 'e381e3698f67d4a140fa71fcd584e873a2394688'},
#  {'date': 'Thu Jun 23 10:13:48 2022 -0300', 'dataStamp': 1655990028.0, 'similarity': 0.8616104868913858, 'reasonSegment': 1, 'message': '', 'commitId': '4b44fda16bb53ccf930c8fa11873fafa7040a586'},
#  {'date': 'Wed Jun 29 11:10:36 2022 -0300', 'dataStamp': 1656511836.0, 'similarity': 0.8612879071508798, 'reasonSegment': 1, 'message': '', 'commitId': 'e70ab24a48e435ab5f6f9246bdb4336fb634defe'},
#  {'date': 'Fri Jun 24 17:35:36 2022 +0800', 'dataStamp': 1656063336.0, 'similarity': 0.8608874742557574, 'reasonSegment': 1, 'message': '', 'commitId': 'af5bf52ddf23e180725e9f0b2a03050b78de6554'},
#  {'date': 'Fri Jul 15 17:57:26 2022 +0800', 'dataStamp': 1657879046.0, 'similarity': 0.8634741784037558, 'reasonSegment': 1, 'message': '', 'commitId': 'd3f965dfe793e279fdf77afe7fe833b5eda1008c'},
#  {'date': 'Mon Aug 1 17:35:48 2022 +0800', 'dataStamp': 1659346548.0, 'similarity': 0.8634741784037558, 'reasonSegment': 1, 'message': '', 'commitId': '78deee68460a6b93dfec61e94052ab6484914242'},
#  {'date': 'Tue Aug 2 17:20:58 2022 +0800', 'dataStamp': 1659432058.0, 'similarity': 0.8634741784037558, 'reasonSegment': 1, 'message': '', 'commitId': 'cffaf95d00a39908fa4687afa4e21cd08cb86949'},
#  {'date': 'Fri Sep 2 16:57:43 2022 -0300', 'dataStamp': 1662148663.0, 'similarity': 0.8601084720403965, 'reasonSegment': 1, 'message': '', 'commitId': 'e0fcf07cf908cd0fd74b65fa8548e284779048d0'},
#  {'date': 'Thu Sep 8 10:13:51 2022 -0300', 'dataStamp': 1662642831.0, 'similarity': 0.856, 'reasonSegment': 1, 'message': '', 'commitId': '87ab2e3a2dd00537d66ac1c06362673af0c5d7ee'},
#  {'date': 'Wed Sep 14 09:32:59 2022 -0300', 'dataStamp': 1663158779.0, 'similarity': 0.8597606581899776, 'reasonSegment': 1, 'message': '', 'commitId': 'dca522d7d340bfafc02792e2e9a9ef21ab0ec274'},
#  {'date': 'Fri Sep 16 14:39:58 2022 -0300', 'dataStamp': 1663349998.0, 'similarity': 0.8549405646359584, 'reasonSegment': 1, 'message': '', 'commitId': 'c20ad3733af2084602dcaf0415eaea67993fe8f7'},
#  {'date': 'Mon Sep 26 15:23:59 2022 -0300', 'dataStamp': 1664216639.0, 'similarity': 0.8553903345724907, 'reasonSegment': 1, 'message': '', 'commitId': '129f09f88bb4081f036264b66677bebb3a2b5071'},
#  {'date': 'Wed Oct 5 22:23:07 2022 +0200', 'dataStamp': 1665001387.0, 'similarity': 0.8526471677156608, 'reasonSegment': 1, 'message': '', 'commitId': '1c29e2806a941a2240443511f01f2fe2c56a8e61'},
#  {'date': 'Wed Oct 12 10:01:10 2022 +0800', 'dataStamp': 1665540070.0, 'similarity': 0.8514137867307336, 'reasonSegment': 1, 'message': '', 'commitId': '56000cbf3ecdbbd4ad19f3a8365c6b5284430820'},
#  {'date': 'Mon Nov 7 14:19:26 2022 +0800', 'dataStamp': 1667801966.0, 'similarity': 0.8503413914006274, 'reasonSegment': 1, 'message': '', 'commitId': '2cd457e07c29af3576bee1c08eae66422f26eced'},
#  {'date': 'Mon Nov 21 21:41:00 2022 +0800', 'dataStamp': 1669038060.0, 'similarity': 0.8492443789163288, 'reasonSegment': 1, 'message': '', 'commitId': 'fcbf1bc8904ce219107734ff01538ccc1c001f0f'},
#  {'date': 'Wed Dec 7 13:49:15 2022 +0800', 'dataStamp': 1670392155.0, 'similarity': 0.8507021433850702, 'reasonSegment': 1, 'message': '', 'commitId': 'b88398c3c6ea5723d9d3cef54813c9c259229fb7'},
#  {'date': 'Thu Dec 29 18:13:09 2022 +0800', 'dataStamp': 1672308789.0, 'similarity': 0.9007760532150776, 'reasonSegment': 0, 'message': '', 'commitId': '32e6dee548d171c232299f892bed91e4e4ab5d32'},
#  {'date': 'Mon Jan 2 08:51:05 2023 +0100', 'dataStamp': 1672645865.0, 'similarity': 0.9007760532150776, 'reasonSegment': 1, 'message': '', 'commitId': 'dbc10c2eed3df314586c7b9ac6292083204f1f68'},
#  {'date': 'Fri Jan 6 23:53:25 2023 +0300', 'dataStamp': 1673038405.0, 'similarity': 0.8968692449355433, 'reasonSegment': 1, 'message': '', 'commitId': 'aaaef30be66ab7291732f3fb634afdd0210b983b'},
#  {'date': 'Sat Jan 14 13:51:26 2023 +0100', 'dataStamp': 1673700686.0, 'similarity': 0.899057127010538, 'reasonSegment': 1, 'message': '', 'commitId': '0f2f5fbbe0f733caa3bf6486af65f8f9339110ee'},
#  {'date': 'Mon Jan 23 00:30:26 2023 +0200', 'dataStamp': 1674426626.0, 'similarity': 0.8900638103919781, 'reasonSegment': 1, 'message': '', 'commitId': 'd36ca18bff8b71c1c3f8d44ae096da3fab6b8c7c'},
#  {'date': 'Fri Feb 17 00:16:29 2023 +0200', 'dataStamp': 1676585789.0, 'similarity': 0.8942130482860302, 'reasonSegment': 1, 'message': '', 'commitId': '609f7bd8fd35b1d76086d7f822deb4e1260b6e47'},
#  {'date': 'Wed Mar 8 21:37:36 2023 +0200', 'dataStamp': 1678304256.0, 'similarity': 0.8996117581808097, 'reasonSegment': 1, 'message': '', 'commitId': 'cba0287439c1142ecde4cf83e596d8fdb91caa72'},
#  {'date': 'Wed Mar 22 15:22:13 2023 -0300', 'dataStamp': 1679509333.0, 'similarity': 0.8977859778597786, 'reasonSegment': 1, 'message': '', 'commitId': 'cb65cded8825eba47d5fde6f4542e66af7807b04'},
#  {'date': 'Mon Mar 27 09:33:17 2023 +0800', 'dataStamp': 1679880797.0, 'similarity': 0.8973082595870207, 'reasonSegment': 1, 'message': '', 'commitId': '07ac2cd57aaba0f2e1776ad36ddbed85475a753a'},
#  {'date': 'Tue Apr 4 17:12:52 2023 +0300', 'dataStamp': 1680617572.0, 'similarity': 0.8906734805621463, 'reasonSegment': 1, 'message': '', 'commitId': 'd7a85242de46fa47f4b0716ce8f644bb8c6672bc'},
#  {'date': 'Wed Apr 12 14:39:59 2023 +0800', 'dataStamp': 1681281599.0, 'similarity': 0.8971428571428571, 'reasonSegment': 1, 'message': '', 'commitId': '7934a1cea13437ee48067186e853f94e556178ea'},
#  {'date': 'Thu Apr 13 14:45:18 2023 +0200', 'dataStamp': 1681389918.0, 'similarity': 0.8962020648967551, 'reasonSegment': 1, 'message': '', 'commitId': '9c11bfce8041e8d110b870d0b8ebffbefc9ea5e0'},
#  {'date': 'Sat Apr 15 06:47:28 2023 +0800', 'dataStamp': 1681512448.0, 'similarity': 0.896036866359447, 'reasonSegment': 1, 'message': '', 'commitId': 'a00daa4d97c19b4fe2bd0c9c8af7ec02705fd4d4'},
#  {'date': 'Fri Apr 21 17:37:17 2023 +0300', 'dataStamp': 1682087837.0, 'similarity': 0.8894160583941606, 'reasonSegment': 1, 'message': '', 'commitId': '0211bcf0305ab5f5b53747aae1b3d01636d527f8'},
#  {'date': 'Sun Apr 23 17:47:00 2023 +0800', 'dataStamp': 1682243220.0, 'similarity': 0.8958333333333334, 'reasonSegment': 1, 'message': '2: Defect added.', 'commitId': 'c2e35a42b0102db0c0053289b3129b7e05e065d8',"offset_x": 50, "offset_y": 0.08},
#  {'date': 'Fri May 5 16:50:18 2023 +0300', 'dataStamp': 1683294618.0, 'similarity': 0.8892133601022084, 'reasonSegment': 1, 'message': '', 'commitId': 'dd3471bc22dd222a6ae71551bf7b879b72bbb152'},
#  {'date': 'Wed May 10 11:55:23 2023 +0500', 'dataStamp': 1683701723.0, 'similarity': 0.8876117496807152, 'reasonSegment': 1, 'message': '', 'commitId': '8d9b785bd7495f4719ebe79739e9a6a5acd4df42'},
#  {'date': 'Fri May 12 14:28:26 2023 +0800', 'dataStamp': 1683872906.0, 'similarity': 0.89486282452587, 'reasonSegment': 1, 'message': '', 'commitId': 'dcd4640a57602fb9f741ca13717fca6e070c849b'},
#  {'date': 'Fri May 12 22:25:32 2023 +0800', 'dataStamp': 1683901532.0, 'similarity': 0.8932449843548684, 'reasonSegment': 1, 'message': '', 'commitId': '67ada52808a6cca44c684ba9e37ca85ceb188cf2'},
#  {'date': 'Mon May 15 14:42:19 2023 +0800', 'dataStamp': 1684132939.0, 'similarity': 0.8920161883738043, 'reasonSegment': 1, 'message': '', 'commitId': 'e26ce5816e28c60cc150e88579c8707f7ecb90c3'},
#  {'date': 'Tue May 16 13:26:22 2023 +0300', 'dataStamp': 1684232782.0, 'similarity': 0.8925680647534953, 'reasonSegment': 1, 'message': '', 'commitId': 'b341a0495541c06d5ebac5a9cab7431bfae39954'},
#  {'date': 'Thu May 18 09:44:01 2023 +0800', 'dataStamp': 1684374241.0, 'similarity': 0.8925087428676606, 'reasonSegment': 1, 'message': '', 'commitId': 'd4d25d26600a217eec4bc1f7afa033aabb11dda7'},
#  {'date': 'Thu May 18 10:00:17 2023 +0800', 'dataStamp': 1684375217.0, 'similarity': 0.891832229580574, 'reasonSegment': 1, 'message': '', 'commitId': 'bf5ee410097e64691927ce028f2b7341720e5092'},
#  {'date': 'Thu May 18 19:33:44 2023 +0300', 'dataStamp': 1684427624.0, 'similarity': 0.8940287504607446, 'reasonSegment': 1, 'message': '', 'commitId': '9c48b016a93fbb3c1604703a41f0490d21957920'},
#  {'date': 'Mon May 22 17:33:24 2023 +0200', 'dataStamp': 1684769604.0, 'similarity': 0.8852668002185394, 'reasonSegment': 1, 'message': '', 'commitId': '732a7be1877b973e2ce885b680e7c038323d34fb'},
#  {'date': 'Wed May 24 09:20:53 2023 +0200', 'dataStamp': 1684912853.0, 'similarity': 0.8874293012224047, 'reasonSegment': 1, 'message': '', 'commitId': '2fdf4b5dac41b9f123da53f052b638f640f93479'},
#  {'date': 'Wed May 24 19:34:12 2023 +0800', 'dataStamp': 1684928052.0, 'similarity': 0.8850846840284101, 'reasonSegment': 1, 'message': '', 'commitId': '28015597eedd0a7ce27378b97cbbbd9bfd1f1a07'},
#  {'date': 'Wed May 31 11:12:53 2023 +0800', 'dataStamp': 1685502773.0, 'similarity': 0.8850846840284101, 'reasonSegment': 1, 'message': '', 'commitId': '65483e972ed80b04f8b6d6a659ab1b2203a002d9'},
#  {'date': 'Thu Jun 1 15:24:31 2023 +0800', 'dataStamp': 1685604271.0, 'similarity': 0.8841741030777636, 'reasonSegment': 1, 'message': '', 'commitId': '070e410c69473ea08ecda7905ea46dc87267fa67'},
#  {'date': 'Thu Jun 1 23:19:19 2023 +0300', 'dataStamp': 1685650759.0, 'similarity': 0.875970391767467, 'reasonSegment': 1, 'message': '', 'commitId': '7de26a17765fffdac1e6d3d37507b58f1974c48d'},
#  {'date': 'Tue Jun 6 17:56:36 2023 +0800', 'dataStamp': 1686045396.0, 'similarity': 0.8861313868613139, 'reasonSegment': 1, 'message': '', 'commitId': '48381d4c8608acbbe446d585b198dbffcb456ac0'},
#  {'date': 'Wed Jun 7 10:22:14 2023 +0800', 'dataStamp': 1686104534.0, 'similarity': 0.837741878217646, 'reasonSegment': 1, 'message': '', 'commitId': 'b5411da770b1251bc05cfc61215777286748a285'},
#  {'date': 'Wed Jun 7 23:04:56 2023 +0200', 'dataStamp': 1686171896.0, 'similarity': 0.8852189781021897, 'reasonSegment': 1, 'message': '', 'commitId': '641aca00d81022744186ffca5e7267a58c9fd6c9'},
#  {'date': 'Fri Jul 7 16:20:55 2023 +0300', 'dataStamp': 1688736055.0, 'similarity': 0.875970391767467, 'reasonSegment': 1, 'message': '', 'commitId': '77895f2555e944712d5409ddf81d0b21ac8faded'},
#  {'date': 'Fri Jul 14 17:19:50 2023 +0800', 'dataStamp': 1689326390.0, 'similarity': 0.875970391767467, 'reasonSegment': 1, 'message': '', 'commitId': 'fea73cf17d20d3fd3914a34ad508a0d608cf4493'},
#  {'date': 'Tue Jul 18 15:43:09 2023 +0200', 'dataStamp': 1689687789.0, 'similarity': 0.888177159590044, 'reasonSegment': 1, 'message': '', 'commitId': '0a00c392822ac30e65d5b16cffb93a7b5c7d474d'},
#  {'date': 'Wed Jul 19 14:11:10 2023 +0200', 'dataStamp': 1689768670.0, 'similarity': 0.8894610998712525, 'reasonSegment': 1, 'message': '', 'commitId': '0cd23511341de3819835ff060bf40958ed2fe7c3'},
#  {'date': 'Wed Jul 19 14:21:26 2023 +0200', 'dataStamp': 1689769286.0, 'similarity': 0.888177159590044, 'reasonSegment': 1, 'message': '', 'commitId': 'f29a9ed9d5769725e3b7148707077320fe63cdb0'},
#  {'date': 'Thu Jul 20 14:33:21 2023 +0200', 'dataStamp': 1689856401.0, 'similarity': 0.8894610998712525, 'reasonSegment': 1, 'message': '', 'commitId': 'f2a32e8ed265b6236f9219e82f249e39ad799360'},
#  {'date': 'Thu Jul 20 20:08:00 2023 +0200', 'dataStamp': 1689876480.0, 'similarity': 0.8694767979293769, 'reasonSegment': 1, 'message': '', 'commitId': 'bf16417513dbf63cdc6c4e2603848529020a9438'},
#  {'date': 'Thu Jul 20 21:19:08 2023 +0200', 'dataStamp': 1689880748.0, 'similarity': 0.8896247240618101, 'reasonSegment': 1, 'message': '', 'commitId': 'e1e4c64a30585adfce25aa00aacaed1dfd3e6a2d'},
#  {'date': 'Mon Jul 24 23:57:09 2023 +0300', 'dataStamp': 1690232229.0, 'similarity': 0.8772151898734177, 'reasonSegment': 1, 'message': '', 'commitId': 'deaac9bd73c9230d291afeecd138bafcc90b9e6a'},
#  {'date': 'Thu Jul 27 15:19:57 2023 +0200', 'dataStamp': 1690463997.0, 'similarity': 0.8909157914133039, 'reasonSegment': 1, 'message': '', 'commitId': 'cbfca8c043d04ee3ebe93424a3b2ec383a1f5a05'},
#  {'date': 'Fri Aug 18 21:10:20 2023 +0300', 'dataStamp': 1692382220.0, 'similarity': 0.8863844603261866, 'reasonSegment': 1, 'message': '', 'commitId': 'b0d4a22aa850db1a6f81637db7f011a0f86d3225'},
#  {'date': 'Wed Aug 23 12:09:40 2023 +0300', 'dataStamp': 1692781780.0, 'similarity': 0.8846153846153846, 'reasonSegment': 1, 'message': '', 'commitId': '39a48179ea29d672e4f3e5864e850b3019bb14cb'},
#  {'date': 'Fri Aug 25 15:08:49 2023 +0800', 'dataStamp': 1692947329.0, 'similarity': 0.8904840787778391, 'reasonSegment': 1, 'message': '', 'commitId': 'fc1738188e0203bd9fc46b9d39a595d191abc9c0'},
#  {'date': 'Tue Aug 29 23:21:36 2023 +0300', 'dataStamp': 1693340496.0, 'similarity': 0.8844322344322344, 'reasonSegment': 1, 'message': '', 'commitId': '54ac4a85277a4255c562785b6c7c58ad054bd435'},
#  {'date': 'Wed Sep 6 09:08:22 2023 +0200', 'dataStamp': 1693984102.0, 'similarity': 0.8840102451518478, 'reasonSegment': 1, 'message': '', 'commitId': 'e794143ae15aac5dc2ef1e7980189e8cef8c37e8'},
#  {'date': 'Fri Sep 8 12:43:05 2023 +0400', 'dataStamp': 1694162585.0, 'similarity': 0.8767123287671232, 'reasonSegment': 1, 'message': '', 'commitId': 'e4866adc2f8714b1f5471aeb483a339b82a379b8'},
#  {'date': 'Thu Sep 14 19:43:44 2023 +0400', 'dataStamp': 1694706224.0, 'similarity': 0.8741258741258742, 'reasonSegment': 1, 'message': '', 'commitId': '97881ff3ca6e61d46ffd3e20b4c9a1059bf5d14b'},
#  {'date': 'Fri Sep 15 13:22:39 2023 +0300', 'dataStamp': 1694773359.0, 'similarity': 0.8733223018937305, 'reasonSegment': 1, 'message': '', 'commitId': '14983ec14a66e4bc2e4aef853ffc167e53a01fa7'},
#  {'date': 'Fri Sep 15 14:34:11 2023 +0400', 'dataStamp': 1694774051.0, 'similarity': 0.8739650413983441, 'reasonSegment': 1, 'message': '', 'commitId': '45d44df11d1f6d4c8481215555d4c222abedd1a8'},
#  {'date': 'Sun Sep 17 19:30:12 2023 +0200', 'dataStamp': 1694971812.0, 'similarity': 0.880466472303207, 'reasonSegment': 1, 'message': '', 'commitId': 'f66d9e76fe5d152914aafc1a1c6e40fb65dc89ec'},
#  {'date': 'Tue Sep 19 18:01:30 2023 +0400', 'dataStamp': 1695132090.0, 'similarity': 0.8739650413983441, 'reasonSegment': 1, 'message': '', 'commitId': '8670efbfa004fb1d79d138b167ae9606c2bbd050'},
#  {'date': 'Tue Sep 19 18:02:57 2023 +0400', 'dataStamp': 1695132177.0, 'similarity': 0.8739650413983441, 'reasonSegment': 1, 'message': '', 'commitId': '98706cd215c0585d0369ea1953df1a51fe7d8f7a'},
#  {'date': 'Tue Sep 19 20:44:53 2023 +0400', 'dataStamp': 1695141893.0, 'similarity': 0.8737810487580496, 'reasonSegment': 1, 'message': '', 'commitId': '69889d14a3be9da8ba5e8de742bb5e6a22748baa'},
#  {'date': 'Mon Sep 25 18:19:26 2023 +0300', 'dataStamp': 1695655166.0, 'similarity': 0.8711151736745887, 'reasonSegment': 1, 'message': '', 'commitId': 'b1f144ab8b24a6500eacdd4dcfac6515d28ded0f'},
#  {'date': 'Tue Sep 26 19:09:53 2023 +0300', 'dataStamp': 1695744593.0, 'similarity': 0.8706613080014615, 'reasonSegment': 1, 'message': '', 'commitId': '1d0e789e4d6326c4e337f9d207a8c6dfbf17bf4c'},
#  {'date': 'Fri Sep 29 10:33:11 2023 +0200', 'dataStamp': 1695976391.0, 'similarity': 0.8737810487580496, 'reasonSegment': 1, 'message': '', 'commitId': 'c64e599e811bc28ff9a19a2bbae696a0f230b90e'},
#  {'date': 'Fri Sep 29 11:36:32 2023 +0200', 'dataStamp': 1695980192.0, 'similarity': 0.8706613080014615, 'reasonSegment': 1, 'message': '', 'commitId': 'ce5bd0a3ceca714d0ea6ad9e5b16f7f9874be62d'},
#  {'date': 'Wed Oct 25 17:12:28 2023 +0800', 'dataStamp': 1698225148.0, 'similarity': 0.8381882770870337, 'reasonSegment': 1, 'message': '', 'commitId': 'afec6fa2f6c547c52479332df1d92703925a0e8d'},
#  {'date': 'Sun Nov 19 22:08:42 2023 +0100', 'dataStamp': 1700428122.0, 'similarity': 0.8716166788588149, 'reasonSegment': 1, 'message': '', 'commitId': 'e73bf716ae113008ffb936b30b27816ce775ce1d'},
#  {'date': 'Mon Nov 20 17:05:10 2023 +0200', 'dataStamp': 1700492710.0, 'similarity': 0.8364312267657993, 'reasonSegment': 1, 'message': '', 'commitId': '7fdc650448f7173204d98b0978c7186dd542ad47'},
#  {'date': 'Wed Nov 22 11:50:40 2023 -0300', 'dataStamp': 1700664640.0, 'similarity': 0.8392603129445235, 'reasonSegment': 1, 'message': '', 'commitId': '6c9417efe08cb52f9daa3aaa56377244232b92fe'},
#  {'date': 'Fri Nov 24 14:52:29 2023 -0300', 'dataStamp': 1700848349.0, 'similarity': 0.8383031593894213, 'reasonSegment': 1, 'message': '', 'commitId': '839f9dbedbded958ac9162e4f7e0d66acd49a002'},
#  {'date': 'Mon Nov 27 09:55:07 2023 +0300', 'dataStamp': 1701068107.0, 'similarity': 0.8392603129445235, 'reasonSegment': 1, 'message': '', 'commitId': '923898eadf0a3a67668217cc751f2633138fa5d6'},
#  {'date': 'Wed Nov 29 14:10:16 2023 +0300', 'dataStamp': 1701256216.0, 'similarity': 0.8383031593894213, 'reasonSegment': 1, 'message': '', 'commitId': 'ccef91437d085bff70e904f933a84d8665dce7da'},
#  {'date': 'Fri Dec 1 11:11:02 2023 +0300', 'dataStamp': 1701418262.0, 'similarity': 0.8368430366306848, 'reasonSegment': 1, 'message': '', 'commitId': '6b17920fea38932442c07d183b00f68f8da8091e'},
#  {'date': 'Sun Dec 3 19:17:46 2023 +0100', 'dataStamp': 1701627466.0, 'similarity': 0.8333920394505108, 'reasonSegment': 1, 'message': '3: Defect fixed.', 'commitId': '423b586c56d52716a6968c751d54852d5b71280e',"offset_x": -200, "offset_y": -0.13},
#  {'date': 'Tue Dec 5 19:01:08 2023 +0200', 'dataStamp': 1701795668.0, 'similarity': 0.8348348348348348, 'reasonSegment': 1, 'message': '', 'commitId': '938508b270c40bef20cf3f41e7344abfa9ceac73'},
#  {'date': 'Wed Dec 6 11:45:41 2023 +0200', 'dataStamp': 1701855941.0, 'similarity': 0.8333920394505108, 'reasonSegment': 1, 'message': '', 'commitId': '28ff53e99ca5d0c66b7bab95eba694808fa4fff6'},
#  {'date': 'Wed Dec 6 15:28:28 2023 +0800', 'dataStamp': 1701847708.0, 'similarity': 0.8329225352112676, 'reasonSegment': 1, 'message': '', 'commitId': '68da627b4dc80fe1e67b12a80cfe959e92c133e1'}]



# 调用函数
plot_similarity(data, 'iotagent-json', 'iotagent-ul')
