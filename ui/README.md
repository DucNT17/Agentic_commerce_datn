# Frontend - E-Commerce Agentic AI

Giao diện người dùng hiện đại cho hệ thống thương mại điện tử được hỗ trợ bởi AI.

## 🎨 Tech Stack

- **Framework**: React 18+ / Vue 3+ / Next.js 14+
- **Language**: TypeScript
- **Styling**: TailwindCSS
- **State Management**: Redux Toolkit / Zustand / Pinia
- **HTTP Client**: Axios
- **Form Handling**: React Hook Form / Formik
- **UI Components**: shadcn/ui / Ant Design / Material-UI
- **Testing**: Vitest / Jest + React Testing Library

## 📁 Cấu trúc dự án

```
ui/
├── public/              # Static assets
├── src/
│   ├── assets/         # Images, fonts, etc.
│   ├── components/     # Reusable components
│   │   ├── common/    # Common UI components
│   │   ├── layout/    # Layout components
│   │   └── features/  # Feature-specific components
│   ├── pages/          # Page components
│   ├── hooks/          # Custom React hooks
│   ├── services/       # API services
│   ├── store/          # State management
│   ├── types/          # TypeScript types
│   ├── utils/          # Utility functions
│   ├── constants/      # Constants
│   ├── styles/         # Global styles
│   ├── App.tsx         # Root component
│   └── main.tsx        # Entry point
├── .env.example        # Environment variables template
├── package.json        # Dependencies
├── tsconfig.json       # TypeScript config
├── vite.config.ts      # Vite config (if using Vite)
└── README.md           # This file
```

## 🚀 Cài đặt và Chạy

### 1. Cài đặt dependencies

```bash
npm install
# hoặc
yarn install
# hoặc
pnpm install
```

### 2. Cấu hình môi trường

```bash
cp .env.example .env
```

Chỉnh sửa file `.env`:

```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=E-Commerce AI
VITE_ENABLE_ANALYTICS=false
```

### 3. Chạy development server

```bash
npm run dev
# hoặc
yarn dev
```

Ứng dụng sẽ chạy tại: <http://localhost:3000> (hoặc 5173 nếu dùng Vite)

### 4. Build cho production

```bash
npm run build
# hoặc
yarn build
```

### 5. Preview production build

```bash
npm run preview
# hoặc
yarn preview
```

## 📦 Scripts

```bash
npm run dev          # Chạy development server
npm run build        # Build cho production
npm run preview      # Preview production build
npm run lint         # Lint code
npm run lint:fix     # Lint và fix lỗi
npm run format       # Format code với Prettier
npm run test         # Chạy tests
npm run test:watch   # Chạy tests trong watch mode
npm run test:coverage # Chạy tests với coverage
npm run type-check   # TypeScript type checking
```

## 🎯 Tính năng chính

### 1. AI Chat Interface

- Giao diện chat với AI agent
- Real-time streaming responses
- Context-aware conversations

### 2. Product Search

- Tìm kiếm sản phẩm với natural language
- Filters và sorting
- Infinite scroll

### 3. Product Details

- Thông tin chi tiết sản phẩm
- Reviews và ratings
- Related products

### 4. AI Recommendations

- Gợi ý sản phẩm cá nhân hóa
- Based on user preferences
- Vector similarity search

### 5. User Dashboard

- Order history
- Saved products
- User preferences

## 🧪 Testing

### Unit Tests

```bash
npm run test
```

### E2E Tests (với Cypress/Playwright)

```bash
npm run test:e2e
```

### Coverage

```bash
npm run test:coverage
```

Mục tiêu coverage: > 80%

## 🎨 Styling Guidelines

### Tailwind Classes Organization

```tsx
<div className="
  // Layout
  flex flex-col items-center justify-between
  
  // Spacing
  p-4 m-2 gap-4
  
  // Sizing
  w-full h-screen max-w-7xl
  
  // Typography
  text-lg font-semibold text-gray-900
  
  // Colors & Effects
  bg-white hover:bg-gray-50
  border border-gray-200 rounded-lg
  shadow-md transition-all
">
  Content
</div>
```

### Component Structure

```tsx
import { FC, useState } from 'react';

interface ProductCardProps {
  id: string;
  name: string;
  price: number;
  onAddToCart?: () => void;
}

export const ProductCard: FC<ProductCardProps> = ({
  id,
  name,
  price,
  onAddToCart
}) => {
  const [loading, setLoading] = useState(false);
  
  const handleClick = async () => {
    setLoading(true);
    // Logic
    setLoading(false);
  };
  
  return (
    <div className="product-card">
      <h3>{name}</h3>
      <p>${price}</p>
      <button onClick={handleClick} disabled={loading}>
        Add to Cart
      </button>
    </div>
  );
};
```

## 🔌 API Integration

### API Service Example

```typescript
// services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle errors
    return Promise.reject(error);
  }
);

export default api;
```

### Product Service Example

```typescript
// services/productService.ts
import api from './api';

export const productService = {
  search: async (query: string) => {
    const response = await api.post('/api/v1/search', { query });
    return response.data;
  },
  
  getById: async (id: string) => {
    const response = await api.get(`/api/v1/products/${id}`);
    return response.data;
  },
  
  getRecommendations: async (productId: string) => {
    const response = await api.get(`/api/v1/recommendations/${productId}`);
    return response.data;
  },
};
```

## 🌐 Environment Variables

```env
# API Configuration
VITE_API_URL=http://localhost:8000
VITE_API_TIMEOUT=10000

# App Configuration
VITE_APP_NAME=E-Commerce AI
VITE_APP_VERSION=1.0.0

# Features
VITE_ENABLE_ANALYTICS=false
VITE_ENABLE_CHAT=true
VITE_ENABLE_RECOMMENDATIONS=true

# External Services
VITE_GOOGLE_ANALYTICS_ID=
VITE_SENTRY_DSN=
```

## 📱 Responsive Design

- **Mobile First**: Design cho mobile trước
- **Breakpoints**:
  - sm: 640px
  - md: 768px
  - lg: 1024px
  - xl: 1280px
  - 2xl: 1536px

## ♿ Accessibility

- Semantic HTML
- ARIA labels
- Keyboard navigation
- Screen reader support
- Color contrast compliance (WCAG AA)

## 🚀 Deployment

### Vercel

```bash
vercel --prod
```

### Netlify

```bash
netlify deploy --prod
```

### Docker

```bash
docker build -t ecommerce-frontend .
docker run -p 3000:3000 ecommerce-frontend
```

## 🐛 Troubleshooting

### Build errors

```bash
# Clear cache
rm -rf node_modules
rm package-lock.json
npm install
```

### Type errors

```bash
npm run type-check
```

## 📚 Resources

- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [TailwindCSS Docs](https://tailwindcss.com/docs)
- [Vite Guide](https://vitejs.dev/guide/)

## 🤝 Contributing

Xem file [CONTRIBUTING.md](../CONTRIBUTING.md) ở root directory.

## 📄 License

MIT License - xem file [LICENSE](../LICENSE).

---

**Happy Coding! 🎉**
