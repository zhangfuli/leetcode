# /* 滑动窗口算法框架 */
# int left = 0, right = 0;
#
# while (left < right && right < s.size()) {
#   // 增大窗口
#   window.add(s[right]);
#   right++;
#
#   while (window needs shrink) {
#       // 缩小窗口
#       window.remove(s[left]);
#       left++;
#   }
# }