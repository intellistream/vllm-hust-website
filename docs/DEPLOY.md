## 📋 Quick Deploy Checklist

### 1. Create GitHub Repository

```bash
# On GitHub.com:
# 1. Create new repository: intellistream/vllm-hust-website
# 2. Make it PUBLIC ✅
# 3. Add description: "vllm-hust website - benchmark-driven serving showcase for domestic hardware"
```

### 2. Push to GitHub

```bash
cd /home/shuhao/vllm-hust-website
git remote add origin git@github.com:intellistream/vllm-hust-website.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages

```
Settings → Pages → Source:
  - Branch: main
  - Folder: / (root)

Save and wait 1-2 minutes.
```

### 4. Access Website

```
https://intellistream.github.io/vllm-hust-website/
```

### 5. Optional: Custom Domain

If you have a domain (e.g., vllm-hust.sage.org.ai):

```
Settings → Pages → Custom domain:
  - Enter: vllm-hust.sage.org.ai
  - Add CNAME record in DNS:
    vllm-hust.sage.org.ai → intellistream.github.io
```

______________________________________________________________________

**Current Status**: ✅ Local files ready, waiting for GitHub push
